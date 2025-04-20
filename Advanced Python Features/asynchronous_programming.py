# This is an easier way to handle multiple concurrent tasks rather than using
# something like threading.

# Asynchronous programming allows me to handle the timing of different events,
# respond to things when data comes in, set up multiple different tasks and
# schedule those to run at the exact asme time, writing code more efficiently.

import asyncio


# Define an asynchronous coroutine:
async def fetch_data() -> dict[str, int]:
    """ simulate an I/O bound task with a delay """

    print("Start fetching data...")
    await asyncio.sleep(2)
    print("Data fetched!")

    return {'data': 42}


# Define an asynchronous coroutine that depends on fetch_data:
async def process_data() -> None:
    """ Simulate a function that waits for the I/O bound task to respond """

    print("Processing data...")
    data = await fetch_data()
    print(f"Processed data: {data['data']}")


async def main() -> None:

    await process_data()


if __name__ == '__main__':

    asyncio.run(main())
