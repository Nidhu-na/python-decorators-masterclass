# 12_Multiple_Decorators / multiple_decorators.py
# Concept: Chaining multiple decorators on a single function

def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1 - Start")
        result = func(*args, **kwargs)
        print("Decorator 1 - End")
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2 - Start")
        result = func(*args, **kwargs)
        print("Decorator 2 - End")
        return result
    return wrapper

# Decorators execute bottom-up (inside-out)
@decorator1
@decorator2
def test():
    print("original function")

test()
# Equivalent to: test = decorator1(decorator2(test))
