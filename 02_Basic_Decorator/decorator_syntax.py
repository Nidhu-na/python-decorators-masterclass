# 02_Basic_Decorator / decorator_syntax.py
# Concept: Applying a decorator using the @ decorator syntax

def decorator(func):
    def execute():
        print("Function start")
        func()
        print("Function end")
        print("This is decorator func")
    return execute

@decorator
def greet():
    print("Hello Bro")

greet()
