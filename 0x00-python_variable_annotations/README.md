# 0x00. Python - Variable Annotations

## Project Overview

This project focuses on using **type annotations** in Python 3. It's designed to deepen understanding of variable annotations, function signatures, complex data types, and duck typing, using tools like `mypy` to validate type correctness.

- **Track:** Back-end
- **Language:** Python
- **Start Date:** Apr 23, 2025, 6:00 PM  
- **End Date:** Apr 24, 2025, 6:00 PM  
- **Checker Released:** Apr 24, 2025, 12:00 AM  
- **Auto Review:** Enabled at deadline

## Concepts

You are expected to be familiar with:

- Advanced Python

## Resources

You are encouraged to read the following materials:

- [Python 3 Typing Documentation](https://docs.python.org/3/library/typing.html)
- [MyPy Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

## Learning Objectives

By the end of this project, you should be able to:

- Use type annotations to specify function signatures and variable types
- Understand and apply duck typing
- Validate Python code using `mypy`

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Files will be interpreted/compiled using **Python 3.7** on **Ubuntu 18.04 LTS**
- Each file must end with a new line
- Shebang line: `#!/usr/bin/env python3`
- Respect `pycodestyle` (version 2.5)
- Files must be executable
- File lengths will be tested with `wc`
- Document all:
  - Modules
  - Classes
  - Functions (inside/outside classes)
- Documentation must be meaningful and descriptive

---

## Tasks

### 0. Basic annotations - add
- Create a type-annotated function `add` that takes two floats and returns their sum as a float.
- File: `0-add.py`

### 1. Basic annotations - concat
- Create a type-annotated function `concat` that takes two strings and returns their concatenation.
- File: `1-concat.py`

### 2. Basic annotations - floor
- Create a type-annotated function `floor` that takes a float and returns the floor value as an integer.
- File: `2-floor.py`

### 3. Basic annotations - to string
- Create a type-annotated function `to_str` that takes a float and returns its string representation.
- File: `3-to_str.py`

### 4. Define variables
- Define the following annotated variables:
  - `a`: int = 1
  - `pi`: float = 3.14
  - `i_understand_annotations`: bool = True
  - `school`: str = "ALX"
- File: `4-define_variables.py`

### 5. Complex types - list of floats
- Write a function `sum_list` that takes a list of floats and returns their sum.
- File: `5-sum_list.py`

### 6. Complex types - mixed list
- Write a function `sum_mixed_list` that takes a list of ints and floats and returns their sum as a float.
- File: `6-sum_mixed_list.py`

### 7. Complex types - string and int/float to tuple
- Write a function `to_kv` that returns a tuple with a string and the square of a number (int/float).
- File: `7-to_kv.py`

### 8. Complex types - functions
- Write a function `make_multiplier` that takes a float and returns a function that multiplies a float by the given multiplier.
- File: `8-make_multiplier.py`

### 9. Let’s duck type an iterable object
- Annotate the function `element_length` to return a list of tuples where each tuple contains an element from the iterable and its length.
- File: `9-element_length.py`

---

## Repository Information

- **Repository:** `alx-backend-python`
- **Directory:** `0x00-python_variable_annotations`

---

Happy Coding! 🐍

Author: Dzeble Kwame Baku
