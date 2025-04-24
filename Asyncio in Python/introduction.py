# ASYNCIO is the choice for tasks that wait a lot, like network requests or
# reading files. It excels at handling many tasks concurrently without using
# much CPU power. This makes my applications more efficient when waiting on a lot
# of different stuff.

# THREADS are suited for tasks that may need to wait but also share data. They can
# run in parallel within the same application, making them useful for tasks that are
# I/O bound but less CPU intensive.

# PROCESSES are used with CUP heavy tasks. Each process operates independently,
# maximizing CPU usage by running in parallel across multiple cores; ideal for
# intensive computations.

# In short:
#       - Use ASYNCIO for managing many waiting tasks efficiently.
#       - Use THREADS for parallel tasks that share data with minimal CPU use.
#       - Use PROCESSES for maximizing performance on CPU internsive tasks.
