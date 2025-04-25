# A future is tipically utilized in lower level libraries.
# A future is a promise of a future result.

import asyncio


async def set_future_result(future, value):

    await asyncio.sleep(2)

    # Set the result of the future
    future.set_result(value)

    print(f"Set the future's result to: {value}")


async def main() -> None:

    # Create a future object
    loop = asyncio.get_running_loop()  # get the event loop
    future = loop.create_future()

    # Schedule setting the future's result
    asyncio.create_task(set_future_result(future, "Future value is ready"))

    # Wait for the future's result
    result = await future

    print(f"Received the future's result: {result}")

# Notice that I didn't await for the task to finish; I awaited the future object.
# As soon as I get the value of the future, the task may or may not be completed.

# I am waiting for a value to be available, not for a task or a coroutine to finish.


if __name__ == '__main__':
    asyncio.run(main())
