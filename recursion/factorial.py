
n = 5

def factorial(n):
    if n == 3:
        return 3 * 2
    elif n == 2:
        return n
    elif n == 1:
        return n
    
    return n * factorial(n-1)

print(factorial(15))