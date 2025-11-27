"""Lesson 24 - Async Basics

Goal: understand async/await, event loops, and concurrent HTTP calls.
"""

import asyncio
import time

import aiohttp

URLS = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/3",
]


async def fetch(session: aiohttp.ClientSession, url: str) -> str:
    async with session.get(url, timeout=5) as response:
        response.raise_for_status()
        data = await response.json()
        return data.get("url", "")


async def gather_all(urls: list[str]) -> list[str]:
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetch(session, url)) for url in urls]
        return await asyncio.gather(*tasks)


async def main() -> None:
    start = time.perf_counter()
    results = await gather_all(URLS)
    duration = time.perf_counter() - start
    print("Fetched:", results)
    print(f"Completed in {duration:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
