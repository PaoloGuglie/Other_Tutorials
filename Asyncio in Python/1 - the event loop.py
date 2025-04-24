# In Python's asyncio, the event loop is the core that manages and distributes tasks.
# Each task takes its turn, and it's either executed immediately or paused if it's
# waiting for something.
# When a task awaits, it steps aside, making room for another task to run, ensuring
# the event loop is always efficiently utilized.
# Once the awaited operation is completed, the task will resume.

import asyncio


async def main():
    """ Coroutine function """

    print("Start of main coroutine!")


if __name__ == '__main__':

    # Start the event loop by running the main coroutine:
    asyncio.run(main())  # pass a coroutine function and returns a coroutine object
