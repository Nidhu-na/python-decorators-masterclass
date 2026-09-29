# 08_Functools_Wraps / functools_wraps.py
# Concept: Preserving original function metadata (__name__, __doc__) using @functools.wraps

from functools import wraps

def fun1(func):
    # @wraps preserves the original function's metadata (__name__, __doc__)
    @wraps(func)
    def fun2(*args, **kwargs):
        return func(*args, **kwargs)
    return fun2

@fun1
def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

print("Function Name:", multiply.__name__)
print("Docstring    :", multiply.__doc__)
print("Result       :", multiply(5, 4))
