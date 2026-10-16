 

# recursio is the concept of a function calling itself. 
# It is used to solve problems that can be broken down into smaller, similar subproblems.
# Recursion typically involves two main components:
# the base case and the recursive case.

#  1.base case - to stop the recursion 
#  2.recuersive case - to continue the recursion

# def print12(n):
#     if n>0:
#         print(n)
#         print12(n-1)
#     else:
#         print("execution completed")
# print12(15)

# def print12(n):
#     if n>0:
#         print12(n-1)
#         print(n)
#     else:
#         print("execution completed")
# print12(15)

# write a program to calculate the sum of first n natural numbers using recursion

# def sum_natural(n):
#     if n==0:
#         return 0

#     return n + sum_natural(n-1)

# print(sum_natural(15))

# write a program to calculate the factorial of a number using recursion

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))

# write a program to find gcd 24 18
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(24,18))


def squre(n):
    return n*n 
print(squre(5))


square = lambda n: n*n
print(square(5))

squre = lambda n:"even" if n%2==0 else "odd"
print(squre(9))


# Higher order function -
# a function that takes another function as an argument or returns a function as a result.
# 1.map
# 2.filter
# 3.reduce
# 4.sorted

arr=[1,2,3,4,5]
print(list(map(lambda x: x*2, arr)))

arr=[1,2,3,4,5]
print(list(filter(lambda x:x%2==0 , arr)))

from functools import reduce
arr=[1,2,3,4,5]
print(reduce(lambda x, y: x + y, arr))


arr=[("siddharth",90),("asif",10),("ajay",30)]
result=sorted(arr,key=lambda a:a[1])
print(result)