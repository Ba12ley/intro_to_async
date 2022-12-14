import asyncio
import datetime
import colorama
import random
# import time


def main():
    #Create async loop
    loop = asyncio.get_event_loop()

    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App started.", flush=True)
    # data = [] # Needs to be a different structure
    data = asyncio.Queue() # If using type annotation, annotate to asyncio.Queue

    # generate_data(20, data)
    # process_data(20, data)

    task1 = loop.create_task(generate_data(20, data))
    task2 = loop.create_task(process_data(20, data))
    final_task = asyncio.gather(task1, task2)
    loop.run_until_complete(final_task)

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + f"App exiting, total time: {dt.total_seconds():,.2f} sec.", flush=True)

#def is not async and methods change to async def

async def generate_data(num: int, data: asyncio.Queue):
    for idx in range(1, num + 1):
        item = idx*idx
        await data.put((item, datetime.datetime.now()))#async changes from append to put. await is the point at which the code is broken up into different calls

        print(colorama.Fore.YELLOW + f" -- generated item {idx}", flush=True)
        await asyncio.sleep(random.random() + .5) #await is the point at which the code is broken up into different calls


async def process_data(num: int, data: asyncio.Queue):
    processed = 0
    while processed < num:
        item = await data.get() #async changes from pop to get. await is the point at which the code is broken up into different calls
        if not item:
            await asyncio.sleep(.01)
            continue

        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t

        print(colorama.Fore.CYAN +
              f" +++ Processed value {value} after {dt.total_seconds():,.2f} sec.", flush=True)
        await asyncio.sleep(.5)


if __name__ == '__main__':
    main()
