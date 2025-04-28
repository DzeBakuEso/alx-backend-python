# 0x01. Python - Async

## Description
This project focuses on asynchronous programming in Python using the `asyncio` module. It covers the basics of writing asynchronous coroutines, executing multiple coroutines concurrently, measuring runtime, and working with asyncio tasks.

## Resources
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Learning Objectives
By the end of this project, you should be able to:
- Explain `async` and `await` syntax
- Execute an async program with `asyncio`
- Run concurrent coroutines
- Create asyncio tasks
- Use the `random` module effectively

## Requirements
### General
- A `README.md` file at the root of the project folder is mandatory
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files should end with a new line
- All files must be executable
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Code should use `pycodestyle` style (version 2.5.x)
- All functions and coroutines must be type-annotated
- All modules and functions should have proper documentation

## Tasks

### 0. The basics of async
Write an asynchronous coroutine `wait_random` that takes an integer `max_delay` (default 10) and waits for a random delay between 0 and `max_delay` seconds before returning the delay.

**File:** `0-basic_async_syntax.py`

### 1. Let's execute multiple coroutines at the same time with async
Write an async routine `wait_n` that takes 2 integers (`n` and `max_delay`) and spawns `wait_random` `n` times with the specified `max_delay`. Returns the list of delays in ascending order.

**File:** `1-concurrent_coroutines.py`

### 2. Measure the runtime
Create a function `measure_time` that measures the total execution time for `wait_n(n, max_delay)` and returns the average time per task.

**File:** `2-measure_runtime.py`

### 3. Tasks
Write a function `task_wait_random` that takes an integer `max_delay` and returns an asyncio.Task.

**File:** `3-tasks.py`

### 4. Tasks
Alter `wait_n` into a new function `task_wait_n` that calls `task_wait_random` instead of `wait_random`.

**File:** `4-tasks.py`

## Project Information
- **Start Date:** Apr 27, 2025 6:00 PM
- **End Date:** Apr 28, 2025 6:00 PM
- **Checker Release:** Apr 28, 2025 12:00 AM
- **Auto Review:** Launched at the deadline

Author:Dzeble Kwame Baku
