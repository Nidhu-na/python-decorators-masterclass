# Python Decorators Masterclass

This repository contains structured, step-by-step examples demonstrating Python Decorators from fundamentals to advanced production patterns.

---

## 📁 Repository Structure

```text
Decorators/
│
├── 01_Function_As_Argument/
│   └── function_as_argument.py       # Passing functions as first-class objects
│
├── 02_Basic_Decorator/
│   ├── manual_decorator.py           # Decorators without syntactic sugar
│   └── decorator_syntax.py           # Decorators using @ syntax
│
├── 03_Decorator_With_Arguments/
│   └── decorator_with_argument.py    # Decorating functions with parameters
│
├── 04_Star_Args/
│   ├── star_args.py                  # Understanding *args tuple packing
│   └── decorator_with_args.py        # Applying *args in decorator wrappers
│
├── 05_Kwargs/
│   └── kwargs.py                     # Understanding **kwargs dictionary packing
│
├── 06_Args_And_Kwargs/
│   ├── args_kwargs.py                # Combining *args and **kwargs
│   └── decorator_args_kwargs.py     # Universal argument handling in decorators
│
├── 07_Return_Values/
│   └── decorator_return_value.py     # Preserving wrapper return values
│
├── 08_Functools_Wraps/
│   └── functools_wraps.py            # Preserving function metadata with @wraps
│
├── 09_Logging_Decorator/
│   └── logging_decorator.py          # Practical function call logger
│
├── 10_Timing_Decorator/
│   └── timing_decorator.py           # Performance & execution time measurement
│
├── 11_Authentication_Decorator/
│   └── authentication_decorator.py   # Role & authentication checks
│
├── 12_Multiple_Decorators/
│   ├── multiple_decorators.py        # Stacking multiple decorators
│   └── decorator_order.py            # Execution order in stacked decorators
│
└── 13_Decorator_Mini_Project/
    └── bank_account_decorators.py    # Banking application mini-project
```

---

## 🚀 How to Run

Navigate to any subfolder and run the script with Python:

```bash
python 13_Decorator_Mini_Project/bank_account_decorators.py
```
