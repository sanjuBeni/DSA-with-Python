# 153/1634
"""
    153 = 1^3 + 5^3 + 3^3
    1634 = 1^4 + 6^4 + 3^4 + 4^4
"""

"""
    TC: O(log10(n))
    SC: O(1)
"""

def is_armstrong_number(n):
    num = n
    total = 0
    # power = len(str(n))
    power = digit_count(n)
    print(power)
    while num > 0:
        mod = num % 10
        total = total + (mod**power)
        num = num // 10

    return n == total


def digit_count(num):
    digit = 0
    n = num
    while n > 0:
        digit = digit + 1
        n = n // 10

    return digit

# print(is_armstrong_number(153))
# print(is_armstrong_number(1634))
# print(is_armstrong_number(16345))
# print(is_armstrong_number(115132219018763992565095597973971522401))