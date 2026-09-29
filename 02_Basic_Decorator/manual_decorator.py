# 02_Basic_Decorator / manual_decorator.py
# Concept: Creating and applying a decorator manually without using the @ syntax

def greet():
    print("Hello Bro")

def decorator(func):
    def execute():
        print("Function start")
        func()
        print("Function end")
        print("This is decorator func")
    return execute

# Manual decorator wrapping
new_func = decorator(greet)
new_func()
