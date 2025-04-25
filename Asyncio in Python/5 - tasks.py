# A task is a way to schedule a coroutine to run as soon as possible and to allow me
# to run multiple corountines simultaneously.
# As soon as a coroutine is sleeping or waiting, I can execute another task. I am
# never executing tasks at the same time (not using multiple cores).

import asyncio
from time import time


async def fetch_data(my_id, sleep_time):

    print(f"\nCoroutine {my_id} starting to fetch data.")

    await asyncio.sleep(sleep_time)

    return f'Coroutine {my_id} completed the task!'


async def main() -> None:

    starting_time = time()

    # Create tasks for running coroutines concurrently:
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))
    task3 = asyncio.create_task(fetch_data(3, 1))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print("\n")
    print(result1, result2, result3)

    print(f"\nCode excution took {round(time() - starting_time, 1)} seconds.")


if __name__ == '__main__':
    asyncio.run(main())
