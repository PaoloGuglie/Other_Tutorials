import asyncio


# There are two types of coroutines:

# coroutine function:
async def greet() -> None:
    print("Hello!")

# coroutine object: what's returned when I call a coroutine function.


# The object has to be passed to asyncio.run(). It's going to wait for that to
# finish, and it's going to start the event loop to handle the asynchronous program.


# If I try to run:
#       greet()
# I will get a RuntimeWarning: "coroutine 'greet' was
# never awaited". A coroutine object needs to be awaited to get the result of the
# execution.


if __name__ == '__main__':

    asyncio.run(greet())
