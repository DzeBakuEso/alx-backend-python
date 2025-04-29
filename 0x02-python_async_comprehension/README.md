# 0x02. Python - Async Comprehension

## Description

This project focuses on mastering **asynchronous programming** concepts in Python, particularly **asynchronous generators** and **async comprehensions**. It also emphasizes proper type annotations and documentation standards in Python 3.7.

## Project Metadata

- **Track:** Python - Back-end  
- **Weight:** 1  
- **Start Date:** April 28, 2025 6:00 PM  
- **Deadline:** April 29, 2025 6:00 PM  
- **Checker Release:** April 29, 2025 12:00 AM  
- **Auto Review:** Enabled at deadline  

## Resources

- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep530)
- [Type Hints for Generators](https://mypy.readthedocs.io/en/stable/generics.html#generators)

## Learning Objectives

By the end of this project, you should be able to explain:

- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- Python version: `3.7` (Ubuntu 18.04 LTS)
- All files must end with a new line
- First line of all Python files: `#!/usr/bin/env python3`
- All code must follow **pycodestyle** (version `2.5.x`)
- File lengths will be checked with `wc`
- All modules must have a full docstring
- All functions and coroutines must be type-annotated
- A `README.md` file is mandatory

---

## Tasks

### 0. Async Generator

**File:** `0-async_generator.py`

Create a coroutine `async_generator()` that:
- Loops 10 times
- Awaits 1 second per loop
- Yields a random float between 0 and 10

**Usage Example:**
```bash
$ ./0-main.py
[4.4, 6.9, 6.2, 4.5, 4.1, 9.9, 6.7, 9.8, 1.0, 1.3]

Author: Dzeble Kwame Baku
