# 01_Function_As_Argument / function_as_argument.py
# Concept: Passing a function as an argument to another function

def add(a, b):
    print("Sum:", a + b)

def execute(func, a, b):
    print("Execution start:")
    func(a, b)
    print("Execution end")

# Passing 'add' function as an argument
execute(add, 10, 20)
