# Allows for simpler synchronization. Acts as a simple boolean flag, and it allows
# to block areas of my code until the flag is set to be true.

import asyncio


async def waiter(event):

    print(" - Waiting for the event to be set.")

    await event.wait()  # await for the event to be set

    print(" - Event has been set, continuing execution.")


async def setter(event):

    print(" -- Setting the event...")

    await asyncio.sleep(2)
    event.set()  # set the event

    print(" -- Event set!")


async def main() -> None:

    event = asyncio.Event()

    await asyncio.gather(waiter(event), setter(event))

    # The first coroutine is started, but then it's stopped while waiting for the event
    # to be set. The second coroutine is started, it sets the event and ends. Control
    # returns to the first coroutine, which finally ends its execution.


if __name__ == '__main__':
    asyncio.run(main())
