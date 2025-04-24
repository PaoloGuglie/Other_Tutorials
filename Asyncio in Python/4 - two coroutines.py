import asyncio
from time import time


async def fetch_data(delay, item_id):
    """ Define a coroutine that simulates a time-consumint task """

    print(f"Fetching data for id: {item_id}")

    await asyncio.sleep(delay)

    print(f"Data fetched for id {item_id}")

    return {'data': 'some data...', 'id': item_id}


async def main() -> None:

    starting_time = time()

    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)

    result1 = await task1
    print(f"Received result: {result1}\n")

    result2 = await task2
    print(f"Received result: {result2}\n")

    print(f"Running the code took {round(time() - starting_time, 1)} seconds")

# This code has no performance advantage.


if __name__ == '__main__':
    asyncio.run(main())
