# TaskGroup provides some built-in error handling, so it's preferred over using
# gather(). If any of the tasks inside the TaskGroup were to fail, it will cancel
# all the other tasks. Tipically preferred in robust applications.

# TaskGroup automatically runs tasks concurrently (not at the same time using
# multiple CPU cores).

# "async with" is called an "asynchronous context manager" (probably used to handle
# exceptions and errors with the context manager methods).

import asyncio
from time import time


async def fetch_data(my_id, sleep_time):
    print(f"\nCoroutine {my_id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return f'Coroutine {my_id} completed the task!'


async def main() -> None:

    starting_time = time()

    tasks = []

    async with asyncio.TaskGroup() as tg:

        for index, sleep_time in enumerate([2, 1, 3], start=1):  # (index starts at 1)

            task = tg.create_task(fetch_data(index, sleep_time))

            tasks.append(task)

    # After the TaskGroup block, all tasks have completed:
    for i in tasks: print(f"\nResult: {i.result()}")

    print(f"\nCode execution took {round(time() - starting_time, 1)} seconds.")


if __name__ == '__main__':
    asyncio.run(main())
