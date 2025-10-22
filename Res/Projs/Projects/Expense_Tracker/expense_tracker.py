def add (a,b):
    sum = a + b
    return sum

def subtract (a,b):
    if a > b:
        diff = a - b
    else:
        diff = b-a
    return diff

def multiply (a,b):
    pdt = a * b
    return pdt

def divide (a,b):
    if b == 0:
        raise ZeroDivisionError
    else:
        div = a / b
        return div
    