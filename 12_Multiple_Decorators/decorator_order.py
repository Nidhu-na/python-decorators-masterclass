# 12_Multiple_Decorators / decorator_order.py
# Concept: Real-world example demonstrating how decorator stacking order affects execution

from functools import wraps

is_log = True

def login_req(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print("Checking Login Status...")
        if is_log:
            res = func(*args, **kwargs)
            return res
        else:
            print("Access Denied")
    return wrap

def logger(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print("Executing function:", func.__name__)
        res = func(*args, **kwargs)
        print("Function completed")
        return res
    return wrap

@logger
@login_req
def dashh():
    print("Dashboard loaded")

dashh()
