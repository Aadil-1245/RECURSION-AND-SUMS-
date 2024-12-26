# Fibonacci Series using Recursion method 
def fucn(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fucn(n-1)+fucn(n-2)
print(fucn(5))