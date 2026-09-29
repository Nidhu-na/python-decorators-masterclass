# 09_Logging_Decorator / logging_decorator.py
# Concept: Real-world logging decorator to record function calls, arguments, and completion status

from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("func   : ", func.__name__)
        print("args   : ", args)
        print("Kwargs : ", kwargs)

        x = func(*args, **kwargs)

        print("Function completed")
        return x
    return wrapper

@logger
def deposit(amount):
    return amount

@logger
def add(a, b):
    return a + b

x = deposit(100)
print("res is :  ", x)

print()

x = add(10, 20)
print("res is :  ", x)
