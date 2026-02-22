"""
A simple calculator module with basic arithmetic operations.
Includes input validation and error handling.
"""

def add(a, b):
    """Return the sum of two numbers."""
    _validate_numbers(a, b)
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    _validate_numbers(a, b)
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    _validate_numbers(a, b)
    return a * b

def divide(a, b):
    """Return the division of two numbers. Raises ZeroDivisionError if b is zero."""
    _validate_numbers(a, b)
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def _validate_numbers(a, b):
    """Internal helper to validate inputs are int or float."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float.")
