# 13_Decorator_Mini_Project / bank_account_decorators.py
# Concept: Combining authentication, logging, and timing decorators into a realistic Banking Application

from functools import wraps
import time

islog = True

def login_req(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print("Checking Login Status...")
        if islog:
            print("Login successful. Access granted.")
            res = func(*args, **kwargs)
            return res
        else:
            print("Login required. Access denied.")
    return wrap

def logger(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print("Func Name is :", func.__name__)
        print("Args are   : ", args)
        print("Kwargs are : ", kwargs)

        res = func(*args, **kwargs)
        return res
    return wrap

def timer(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        en = time.time()
        print("total Time of Execution  :", en - st, " Secs")
        return res
    return wrap

@login_req
@logger
@timer
def deposit(amt):
    return amt

@login_req
@logger
@timer
def withdraw(balance, amount):
    return balance - amount

print("\n----- Deposit Operation -----")
print("Deposit result :", deposit(5000))

print("\n----- Withdrawal Operation -----")
print("Withdrawal result :", withdraw(10000, 2500))
