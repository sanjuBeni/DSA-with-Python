number = int(input('Enter a number: '))

"""
    floor division is //
    58//10 it give 5 not 5.8
"""

"""
    Space complecity is O(1)
    Time complexity is this method is O(log10(n))

    10 mean base, & base mean divisional number, 
    if divisional number is 5 then time complexity is O(log5(n)) 
"""

def count_number_digit(num):
    if num >= 0 and num <= 9:
        return 1
    
    digit = 0
    n = num
    while n > 0:
        digit = digit + 1
        n = n // 10
    return digit

print(count_number_digit(num=number))