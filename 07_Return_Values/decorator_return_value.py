# 07_Return_Values / decorator_return_value.py
# Concept: Preserving and returning the wrapped function's return value from the decorator wrapper

def fun1(func):
    def fun2(*args, **kwargs):
        print("Start")
        x = func(*args, **kwargs)
        print("End")
        return x
    return fun2

@fun1
def stud(name, age, cour):
    return f"Name is {name} and Age is {age} course is {cour}"

x = stud("nidhu", age=21, cour="eng")
print(x)
