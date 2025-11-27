# Exercise: API Dashboard

Build a CLI tool that fetches data from a public API and summarizes it locally.

## Requirements

1. Use `requests` to call the GitHub API endpoint `https://api.github.com/repos/{owner}/{repo}`.
2. Accept repository coordinates via CLI arguments (use `argparse`).
3. Display: stars, forks, open issues, last push date, and description.
4. Cache responses by writing JSON to `data/{owner}_{repo}.json` so repeated runs read from disk when `--offline` flag is passed.
5. Handle HTTP errors (`response.raise_for_status()`), timeouts, and missing repositories gracefully.
6. Provide a `--save` flag to append a line to `stats.csv` with repo name and stars.
7. Include environment variable support: `GITHUB_TOKEN` for optional authentication (send as header if present).

## Stretch Ideas

- Add a subcommand to list cached repositories and their star counts.
- Support rate-limit inspection via the `X-RateLimit-Remaining` header.
- Implement exponential backoff when the API returns 429.

## Tips

- Use `requests.get(..., timeout=10)` to avoid hanging.
- Wrap network calls in try/except and show friendly messages.
- Normalize file names with `.replace('/', '_')` before saving.
