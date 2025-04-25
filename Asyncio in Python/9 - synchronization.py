# Synchronization primitives are tools that allow me to synchronize the execution of
# various coroutines, especially in larger programs.

import asyncio

# A shared variable
shared_resource = 0

# An asyncio lock
lock = asyncio.Lock()


async def modify_shared_resource():

    global shared_resource

    async with lock:
        # Acquire the lock by checking if another coroutine is currently using the lock.
        # If it is, it's going to wait until that coroutine is finished. If it's not, it's
        # going to enter the block of code.
        # Everything inside the context manager needs to finish executing before the lock
        # will be released.

        print(f"resource before modification: {shared_resource}")

        shared_resource += 1

        await asyncio.sleep(1)
        print(f"Resource after modification: {shared_resource}")
        print("-----------")


async def main() -> None:

    # Use *() to unpack the generator expression into individual arguments for the
    # .gather() function. Instead of passing a generator expression that creates an
    # iterator producing five instances of the modify_shared_resource() coroutine, I
    # am passing each coroutine as a separate argument.
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))


if __name__ == '__main__':
    asyncio.run(main())
