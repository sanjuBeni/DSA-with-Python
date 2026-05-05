from math import sqrt

number = int(input('Enter a number: '))

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    for i in range(5, int(sqrt(number)) + 1, 2):
        if num % i == 0:
            return False

    return True


data = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Find prime number
def find_prime_nums(data):

    result = []
    for i in range(len(data)):
        if is_prime(data[i]):
            result.append(data[i])

    return result

print(find_prime_nums(data))

# prime number upto n
def find_prime_upto_n(n):

    for i in range(n+1):
        if i == 100:
            break
        if is_prime(i):
            print(i)

find_prime_upto_n(1_000_000)
