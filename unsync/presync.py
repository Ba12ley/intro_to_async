import asyncio
import datetime
import math

import aiohttp
import requests
from unsync import unsync


def main():
    t0 = datetime.datetime.now()

    # Changed this from the video due to changes in Python 3.10:
    # DeprecationWarning: There is no current event loop, loop = asyncio.get_event_loop()
    # loop = asyncio.new_event_loop()

    # tasks = [
    #     loop.create_task(compute_some()),
    #     loop.create_task(compute_some()),
    #     loop.create_task(compute_some()),
    #     loop.create_task(download_some()),
    #     loop.create_task(download_some()),
    #     loop.create_task(download_some_more()),
    #     loop.create_task(download_some_more()),
    #     loop.create_task(wait_some()),
    #     loop.create_task(wait_some()),
    #     loop.create_task(wait_some()),
    #     loop.create_task(wait_some()),
    # ]
    tasks = [
        compute_some(),
        compute_some(),
        compute_some(),
        download_some(),
        download_some(),
        download_some_more(),
        download_some_more(),
        wait_some(),
        wait_some(),
        wait_some(),
        wait_some(),
    ]

    # loop.run_until_complete(asyncio.gather(*tasks))
    [t.result() for t in tasks]

    dt = datetime.datetime.now() - t0
    print(f"Synchronous version done in {dt.total_seconds():,.2f} seconds.")


@unsync(cpu_bound=True) # Will mark for multiprocessing
# async def compute_some():
def compute_some():
    print("Computing...")
    for _ in range(1, 10_000_000):
        math.sqrt(25 ** 25 + .01)


@unsync()
async def download_some():
    print("Downloading...")
    url = 'https://talkpython.fm/episodes/show/174/coming-into-python-from-another-industry-part-2'
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(url) as resp:
            resp.raise_for_status()

            text = await resp.text()

    print(f"Downloaded (more) {len(text):,} characters.")


@unsync() # Will mark for threading
# async def download_some_more():
def download_some_more():
    print("Downloading more ...")
    url = 'https://pythonbytes.fm/episodes/show/92/will-your-python-be-compiled'
    resp = requests.get(url)
    resp.raise_for_status()

    text = resp.text

    print(f"Downloaded {len(text):,} characters.")


@unsync()
async def wait_some():
    print("Waiting...")
    for _ in range(1, 1000):
        await asyncio.sleep(.001)


if __name__ == '__main__':
    main()
