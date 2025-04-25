# A semaphore works very similarly to a lock. However, it allows multiple coroutines
# to have access to the same object at the same time.

# For example, it can be used to limit the network requests sent at the same time.

import asyncio


async def access_resource(semaphore, resource_id):

    async with semaphore:

        # Simulate accessing a limited resource
        print(f" - Accessing resource {resource_id}")
        await asyncio.sleep(1)
        print(f" -- Releasing resource {resource_id}")


async def main() -> None:

    semaphore = asyncio.Semaphore(2)  # allow 2 concurrent accesses

    await asyncio.gather(*(access_resource(semaphore, i) for i in range(1, 6)))


if __name__ == '__main__':
    asyncio.run(main())
