# Concurrency vs Parallelism
# Concurrency: multiple tasks run in overlapping time periods. Only one thread is executing at any given moment.
# Parallelism: multiple tasks run at the same time

# Overhead of managing states of multiple threads more or less remains constant irrespective of the number of threads. So, this overhead can be ignored for large number of threads.

# If there is a shared resource that is shared between the threads, then the tasks need to be synchronized and we need to use a lock such as mutex or semaphore. If the quantity of shared resource is 1 use mutex else use semaphore.