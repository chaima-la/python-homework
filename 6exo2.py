import math 

def fact(n):
    i = n
    f = 1
    print(f"Starting factorial calculation for: {n}")
    
    while i > 0:
        print(f"Current i: {i}, Current f: {f}")
        f = f * i
        i = i - 1
        print(f"Updated f after multiplying by {i+1}: {f} \n")
    
    print(f'The factorial of {n} is {f}')

n = int(input("Enter a number: "))
if n < 0:
    print("Negative number")
else:
    fact(n)
    f = math.factorial(n)
    print(f'Using module: {f}')
