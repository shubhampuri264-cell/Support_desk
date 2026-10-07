"""Small Jira Service Management client: basic auth, get/post/put and JQL paging.

Every other script imports this. Settings come from .env (see .env.example).
Run it directly to check the connection and print the ids Phase 0 asks for:

    python src/jsm.py
"""
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

TIMEOUT = 30


def env(name, default=None):
    value = os.environ.get(name, default)
    if not value:
        sys.exit(f"Missing {name} in .env (copy .env.example to .env and fill it in)")
    return value


def project_key():
    return os.environ.get("JSM_PROJECT_KEY", "SUP")


def _request(method, path, params=None, body=None):
    url = env("JSM_SITE").rstrip("/") + path
    headers = {"Accept": "application/json"}
    if path.startswith("/rest/servicedeskapi/"):
        # A few servicedeskapi endpoints (customer search, knowledge base) are
        # still marked experimental and refuse calls without this header.
        headers["X-ExperimentalApi"] = "opt-in"
    r = requests.request(
        method,
        url,
        auth=(env("JSM_EMAIL"), env("JSM_API_TOKEN")),
        params=params,
        json=body,
        headers=headers,
        timeout=TIMEOUT,
    )
    if not r.ok:
        raise JSMError(method, path, r.status_code, r.text)
    if r.status_code == 204 or not r.content:
        return None
    return r.json()


class JSMError(Exception):
    def __init__(self, method, path, status, text):
        super().__init__(f"{method} {path} failed with {status}: {text[:500]}")
        self.status = status
        self.text = text


def get(path, **params):
    return _request("GET", path, params=params)


def post(path, body):
    return _request("POST", path, body=body)


def put(path, body):
    return _request("PUT", path, body=body)


def search(jql, fields, page_size=50):
    """Yield every issue matching jql from /rest/api/3/search/jql.

    The endpoint pages with nextPageToken until isLast. fields is required:
    without it the endpoint returns only issue ids.
    """
    token = None
    while True:
        params = {"jql": jql, "fields": ",".join(fields), "maxResults": page_size}
        if token:
            params["nextPageToken"] = token
        page = get("/rest/api/3/search/jql", **params)
        yield from page.get("issues", [])
        token = page.get("nextPageToken")
        if page.get("isLast", True) or not token:
            return


def paged(path, **params):
    """Yield every value from a servicedeskapi list endpoint (start/limit paging)."""
    start = 0
    while True:
        page = get(path, start=start, limit=50, **params)
        values = page.get("values", [])
        yield from values
        if page.get("isLastPage", True) or not values:
            return
        start += len(values)


def service_desk_id():
    return env("JSM_SERVICE_DESK_ID")


def request_types(desk_id=None):
    """Map request type name to id for the service desk."""
    desk_id = desk_id or service_desk_id()
    return {
        rt["name"]: rt["id"]
        for rt in paged(f"/rest/servicedeskapi/servicedesk/{desk_id}/requesttype")
    }


def main():
    desks = list(paged("/rest/servicedeskapi/servicedesk"))
    print("Service desks:")
    for d in desks:
        print(f"  id={d['id']}  key={d['projectKey']}  name={d['projectName']}")

    desk = next((d for d in desks if d["projectKey"] == project_key()), None)
    if not desk:
        sys.exit(f"No service desk with project key {project_key()}")

    print(f"\nRequest types for {desk['projectKey']}:")
    for name, rt_id in request_types(desk["id"]).items():
        print(f"  {rt_id:>6}  {name}")

    me = get("/rest/api/3/myself")
    print(f"\nSigned in as {me['displayName']} ({me.get('emailAddress', 'email hidden')})")
    print("\nAdd these to .env:")
    print(f"JSM_SERVICE_DESK_ID={desk['id']}")
    print(f"JSM_ACCOUNT_ID={me['accountId']}")


if __name__ == "__main__":
    main()
