'''
CALCULATOR CLI
================
Goal: Build a CLI that can do addition, subtraction, multiplication, and division.

Requirements:
    Two positional numbers x and y.
    Optional argument -o/--operation with choices: add, sub, mul, div (default: add).
    Optional verbosity flag -v/--verbose to print descriptive output.

Hints:
    Use choices parameter for --operation.
    Use type=float for numbers.
    Access the chosen operation in args.operation.

$ python calc.py 5 3
8

$ python calc.py 5 3 --operation sub
2

$ python calc.py 5 3 --operation mul --verbose
5 * 3 = 15

'''