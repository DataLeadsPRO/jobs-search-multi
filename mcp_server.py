import os
import httpx
from mcp.server.fastmcp import FastMCP

BASE = os.environ.get('DATALEADS_BASE_URL', 'https://data.dataleads.pro/v1')
KEY = os.environ.get('DATALEADS_API_KEY', '')
mcp = FastMCP('Jobs Search API (Multi-Board)')

def _call(path, payload):
    body = {'clientKey': KEY}
    body.update(payload or {})
    r = httpx.post(BASE + path, json=body, headers={'Authorization': 'Bearer ' + KEY}, timeout=120)
    r.raise_for_status()
    return r.json()

TOOLS = [
  {
    "name": "jobs_multi",
    "method": "POST",
    "path": "/jobs/multi",
    "description": "V1 Jobs Multi"
  },
  {
    "name": "jobs_indeed",
    "method": "POST",
    "path": "/jobs/indeed",
    "description": "V1 Jobs Indeed"
  },
  {
    "name": "jobs_linkedin",
    "method": "POST",
    "path": "/jobs/linkedin",
    "description": "V1 Jobs Linkedin"
  },
  {
    "name": "jobs",
    "method": "POST",
    "path": "/jobs",
    "description": "V1 Jobs"
  }
]

def _register():
    import json as _json
    for t in TOOLS:
        def _make(t=t):
            def _tool(payload: dict) -> dict:
                return _call(t['path'], payload)
            _tool.__name__ = t['name']
            _tool.__doc__ = t['description']
            return _tool
        fn = _make()
        mcp.tool()(fn, name=t['name'], description=t['description'])

_register()


if __name__ == '__main__':
    mcp.run()
