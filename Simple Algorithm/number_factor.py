from math import sqrt

num = -99
def factor(n):
    if n < 0:
        return 'Number is -ve value.'
    result = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            result.append(i)
            if n//i != i:
                result.append(n//i)

    return result

print(factor(num))