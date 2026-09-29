# 03_Decorator_With_Arguments / decorator_with_argument.py
# Concept: Decorating functions that accept arguments

def login(func):
    def wrapper(name):
        print("Checking log status...")
        result = func(name)
        print("Function ended with result:", result)
        return result
    return wrapper

@login
def profile(name):
    print("Welcome", name)
    return "MG"

x = profile("Nidhu")
print("Returned value:", x)
