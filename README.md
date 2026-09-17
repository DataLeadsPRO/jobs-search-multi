# Jobs Search API (Multi-Board)

> Search job postings across Indeed, LinkedIn, and more from one request - titles, companies, salaries as JSON.

Part of the **DataLeads** API suite (Jobs category). Requests render in a real browser with anti-bot handling and protected-page support built in - no proxies to manage, no infrastructure to run.

## Endpoints

| Method | Path | Description |
|---|---|---|
| POST | `/jobs/multi` | V1 Jobs Multi |
| POST | `/jobs/indeed` | V1 Jobs Indeed |
| POST | `/jobs/linkedin` | V1 Jobs Linkedin |
| POST | `/jobs` | V1 Jobs |

## Quick start

```bash
curl -X POST https://data.dataleads.pro/v1/jobs/multi \
  -H 'Content-Type: application/json' \
  -d '{"clientKey": "YOUR_CLIENT_KEY", "query": "python developer", "location": "New York, NY"}'
```

Replace `YOUR_CLIENT_KEY` with your key. Get one at [https://data.dataleads.pro](https://data.dataleads.pro) - free tier included.

## MCP server

- **Remote (Streamable HTTP):** `https://data.dataleads.pro/mcp/jobs-search-multi`
- **Stdio (Docker):** `docker run -e DATALEADS_API_KEY=yourkey ghcr.io/dataleads/jobs-search-multi-mcp:latest`

## Pricing

| Tier | Price | Requests |
|---|---|---|
| Free | $0 | 500/mo |
| Starter | $9/mo | 5,000 |
| Pro | $29/mo | 25,000 |
| Business | $99/mo | 100,000 |
| Enterprise | custom | custom |

Full plan details at [https://data.dataleads.pro](https://data.dataleads.pro).

## License

MIT - see [LICENSE](LICENSE).
