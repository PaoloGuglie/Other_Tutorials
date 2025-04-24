import asyncio


# The "await" keyword is used to await a coroutine and allow it to execute and get
# the result. I can only use this keyword inside an asynchronous function or inside
# a coroutine:

async def fetch_data(delay):
    """ Define a coroutine that simulates a time-consuming task """

    print("Fetching data...")
    await asyncio.sleep(delay)
    print("Data fetched!")

    return {'data': 'Some data...'}


async def main():
    """ Define another coroutine that calls the first coroutine """

    print("--- Start of the main coroutine ---")

    task = fetch_data(2)  # returns a coroutine object, not yet being executed.

    # await the fetch_data coroutine, pausing execution of main() until it completes:

    result = await task  # awaits the coroutine for it to actually be executed.

    print(f"received result: {result['data']}")

    print("--- End of main coroutine ---")

# A coroutine doesn't start executing until it's awaited or until it's wrapped in a
# task.


if __name__ == '__main__':
    asyncio.run(main())
