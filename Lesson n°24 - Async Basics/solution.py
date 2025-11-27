"""Lesson 24 - Async Basics (Solution)

Reference implementation for the Async Downloader exercise.
"""

import argparse
import asyncio
import json
from pathlib import Path
from typing import Any

import aiohttp

API_URL = "https://jsonplaceholder.typicode.com/posts/{id}"
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Async downloader")
    parser.add_argument("ids", nargs="+", type=int)
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--limit", type=int, default=3, help="Max concurrent requests")
    return parser

def target_path(item_id: int) -> Path:
    return DATA_DIR / f"post_{item_id}.json"

async def fetch_post(session: aiohttp.ClientSession, item_id: int, semaphore: asyncio.Semaphore) -> tuple[int, bool, str]:
    path = target_path(item_id)
    if path.exists():
        return item_id, True, "cached"
    url = API_URL.format(id=item_id)
    async with semaphore:
        try:
            async with session.get(url, timeout=10) as response:
                response.raise_for_status()
                data = await response.json()
                path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        except Exception as exc:
            return item_id, False, str(exc)
    return item_id, True, "downloaded"

async def run_download(ids: list[int], offline: bool, limit: int) -> tuple[list[tuple[int, bool, str]], float]:
    start = asyncio.get_event_loop().time()
    semaphore = asyncio.Semaphore(limit)
    results: list[tuple[int, bool, str]] = []
    if offline:
        for item_id in ids:
            path = target_path(item_id)
            if path.exists():
                results.append((item_id, True, "cached"))
            else:
                results.append((item_id, False, "missing cache"))
        duration = asyncio.get_event_loop().time() - start
        return results, duration

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_post(session, item_id, semaphore) for item_id in ids]
        results = await asyncio.gather(*tasks)
    duration = asyncio.get_event_loop().time() - start
    return results, duration

def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.offline:
        results, duration = asyncio.run(run_download(args.ids, True, args.limit))
    else:
        results, duration = asyncio.run(run_download(args.ids, False, args.limit))
    successes = sum(1 for _id, ok, _ in results if ok)
    failures = len(results) - successes
    for item_id, ok, status in results:
        status_label = "OK" if ok else "FAIL"
        print(f"{status_label} - Post {item_id}: {status}")
    print(f"Completed in {duration:.2f}s | Successes: {successes} | Failures: {failures}")
    return 0 if failures == 0 else 1

if __name__ == "__main__":
    raise SystemExit(main())
