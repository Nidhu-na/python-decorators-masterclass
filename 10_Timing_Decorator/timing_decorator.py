# 10_Timing_Decorator / timing_decorator.py
# Concept: Building a performance measurement decorator using the time module

import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Func started..")
        st = time.time()
        res = func(*args, **kwargs)
        end = time.time()

        print("function name :", func.__name__)
        print("Time taken : ", (end - st))

        return res
    return wrapper

@timer
def calc():
    tot = 0
    for i in range(20000000):
        tot += 1
    return tot

res = calc()
print("Result : ", res)
