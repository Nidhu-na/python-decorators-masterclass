# 04_Star_Args / star_args.py
# Concept: Understanding variable-length positional arguments (*args)
# *args converts passed arguments into a tuple: (10, 20, 30)

def test(*args):
    print("Received args as tuple:", args)
    for index, arg in enumerate(args):
        print(f"Arg {index}: {arg}")

test(10, 20, 30)
