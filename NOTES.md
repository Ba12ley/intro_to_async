# Async

## Concepts
![](images_for_notes/async_high_level_from_talk_python.jpeg)

### asyncio

Use `async` when defining the function to indicate that it is and async method.

`async def func():`

For the processes to wait on or that can be sliced up use `await`.

`html = await get_html()`

asyncio has various libraries to work with other frameworks and tools, google for available option for Redis, Mongo and the like.

### Threads 
![](images_for_notes/thread_fork_join.jpeg)

Fork->join style of pattern.  Thread process works on the same memory per process.

Starting threads and joining threads, using the daemon arguement to run in the background.
![](images_for_notes/Starting_waiting_threads.png)

Using List comprehensions to group threads

![](images_for_notes/listing_threads_list_comp.png)

### Processes
![](images_for_notes/multi_processes.png)
### The Global Interpreter Lock (GIL)
Is Pythons memory management feature.  

Thread Safety

### Viewing Processes

Use glances `brew install glances`

Run with `glances`

### UnSync

For mixed-mode parallelism

If the @unsync() is applied to a async function an ambient asyncio event loop will run.

For none async functions the @unsync() can still be used, but with the arguement cpu_bound=True.  This will mark it for multiprocessing. No arguement will mark it for threading.




