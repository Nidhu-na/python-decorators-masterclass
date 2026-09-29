# 11_Authentication_Decorator / authentication_decorator.py
# Concept: Access control / login authentication check using decorators

from functools import wraps

is_logged_in = True

def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Checking Login Status...")
        if is_logged_in:
            print("Access granted for:", func.__name__)
            return func(*args, **kwargs)
        else:
            print("Access denied. Login required.")
    return wrapper

@require_login
def dashboard():
    print("Welcome to Dashboard!")

dashboard()
