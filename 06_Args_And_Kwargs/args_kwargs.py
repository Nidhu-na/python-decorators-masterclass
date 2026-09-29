# 06_Args_And_Kwargs / args_kwargs.py
# Concept: Combining *args and **kwargs in a single function signature

def test(*args, **kwargs):
    print("args : ", args)
    print("kwargs : ", kwargs)

test(1, 2, 3, a="nidhu", b="20")
