# 04_Star_Args / decorator_with_args.py
# Concept: Using *args inside a decorator to accept any number of positional arguments

def execute(func):
    def wrap(*args):
        print("Started the program")
        res = func(*args)
        print("Res is", res)
        print("Program is Ended")
        return res
    return wrap

@execute
def add(a, b, c):
    return a + b + c

x = add(10, 20, 30)
print("Final res:", x)
