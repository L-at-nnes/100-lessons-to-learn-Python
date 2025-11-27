# Exercise: Async Downloader

Build an asynchronous downloader that fetches multiple URLs concurrently.

## Requirements

1. Use `aiohttp` to download JSON from multiple endpoints (e.g., `https://jsonplaceholder.typicode.com/posts/{id}`).
2. Accept a list of IDs via CLI arguments (use `argparse`).
3. Limit concurrency with an `asyncio.Semaphore` to avoid overloading the API.
4. Save each response as `data/post_{id}.json` inside a `data` folder.
5. Handle HTTP errors, timeouts, and invalid IDs gracefully.
6. Print a summary of successes vs failures plus total elapsed time.
7. Provide an optional `--offline` flag that reads from disk if the file already exists.

## Stretch Ideas

- Use `asyncio.as_completed` to process results as they finish.
- Add retries with exponential backoff for transient errors.
- Display a progress bar using `tqdm.asyncio`.

## Tips

- Use `asyncio.run()` to start the program.
- Wrap network calls in try/except and return statuses for each ID.
- Create the `data` directory at startup with `mkdir(exist_ok=True)`.
