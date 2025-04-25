# The gather() function is a quick way to concurrently run multiple coroutines.
# Instead of creating multiple tasks, using gather() I can already schedule for
# them to run concurrently and collect the results in a list.
# Each argument is a coroutine.

# It's not good at error handling, and it's not going to automatically cancel other
# coroutines if one of them were to fail.

import asyncio
from time import time


async def fetch_data(my_id, sleep_time):
    print(f"\nCoroutine {my_id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return f'Coroutine {my_id} completed the task!'


async def main() -> None:

    starting_time = time()

    # Run coroutines concurrently and gather ther return values:
    results = await asyncio.gather(fetch_data(1, 2),
                                   fetch_data(2, 3),
                                   fetch_data(3, 1))

    for i in results: print(f"\n{i}")

    print(f"\nCode execution took {round(time() - starting_time, 1)} seconds.")


if __name__ == '__main__':
    asyncio.run(main())
