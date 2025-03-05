def factorial(n):
    if 0 == n or 1 == n:
        return 1
    return n * factorial(n-1)
    

print(factorial(5))