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

### Processes

### The Global Interpreter Lock (GIL)
Is Pythons memory management feature.  

Thread Safety

### Viewing Processes

Use glances `brew install glances`

Run with `glances`






