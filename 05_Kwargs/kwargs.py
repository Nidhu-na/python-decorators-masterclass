# 05_Kwargs / kwargs.py
# Concept: Understanding keyword arguments (**kwargs)
# **kwargs converts keyword arguments into a dictionary: {"name": "Nidhu", "age": 21}

def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

profile(name="nidhu", age=21, id="121")
