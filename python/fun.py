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
