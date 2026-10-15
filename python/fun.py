def add(a,b):
    return a+b

result = add(5, 3)
print(result)  # Output: 8

def subtract(a=10, b=5):
    return a - b

result = subtract()
print(result)  # Output: 2

def add(*args):
    return sum(args)
result = add(1, 2, 3, 4, 5)
print(result)  # Output: 15

def sub(*subt):
    return sum(subt) - max(subt)
result = sub(10, 5, 2)
print(result)  # Output: 17