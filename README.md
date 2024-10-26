# alx-bakend-python


# Advanced Python

## Introduction

Python is a dynamically-typed language. This means that variable types are determined at **run-time**, when values are assigned to variables. Unlike statically-typed languages, where variable types are known at build-time, Python resolves the types dynamically during execution.

For example, consider the following function:

```python
def fn(a, b):
    return a + b
```

In this case, the types of `a` and `b` are not explicitly known until they are assigned values during execution. At build-time, Python does not know the types of these variables.

### Dynamic Typing in Action

Calling the function with a string and an integer will not raise an error until the code is actually executed:

```python
fn("a", 1)
```

When this is run, the following error is raised:

```bash
>>> fn("a", 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

### Python 3 Type Annotations

In Python 3, **type annotations** were introduced, but they do not change the dynamic typing nature of the language. Even with type annotations, Python remains dynamically typed, and types are enforced only during execution, not at build-time.

Type annotations serve two primary purposes:

1. **Code Documentation**: Type annotations provide clear documentation for developers, making it easy to understand what types variables and function arguments should be. This helps reduce bugs and improves collaboration within teams, as developers can read type-annotated code and immediately know the expected types.

    Example of a function with type annotations:

    ```python
    def add(a: float, b: float) -> float:
        """
        Adds two floating-point numbers and returns the result.
        """
        return a + b
    ```

    With this annotation, it's clear that `a` and `b` are expected to be floats, and the function returns a float.

2. **Linting and Validation**: Tools like linters (e.g., `pylint`, `flake8`) and type-checkers (e.g., `mypy`) can be used to validate type-annotated code. These tools help catch potential type-related bugs at build-time before they make it to production, providing an extra layer of assurance in your code quality.

    For example, using `mypy` to validate the following code:

    ```bash
    mypy 0-add.py
    ```

    This will check if the types in the code are correctly used and raise errors if there are any type mismatches.

### Conclusion

Although Python is a dynamically-typed language, type annotations add a layer of clarity and robustness to code by documenting expected types and enabling validation during development. This can significantly accelerate development, reduce runtime errors, and improve the overall quality of code.

Type annotations are not enforced by Python at runtime, but they provide valuable information for developers and tools that can catch errors early, ensuring a smoother and more efficient development process.

## Resources

1. [Python Type Hints Documentation](https://docs.python.org/3/library/typing.html)
2. [MyPy Cheat Sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html)
