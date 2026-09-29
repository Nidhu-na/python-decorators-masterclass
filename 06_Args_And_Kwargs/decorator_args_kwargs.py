# 06_Args_And_Kwargs / decorator_args_kwargs.py
# Concept: Universal decorator pattern handling both positional and keyword arguments (*args, **kwargs)

def fun1(func):
    def fun2(*args, **kwargs):
        print("prog start")
        func(*args, **kwargs)
        print("prog ended")
    return fun2

@fun1
def add(a, b, c, d):
    print("a ", a)
    print("b ", b)
    print("c ", c)
    print("d ", d)
    print("a+b", a + b)
    print("c+d ", c + d)
    print("a+b+c+d", a + b + c + d)

add(1, 2, c=4, d=5)
