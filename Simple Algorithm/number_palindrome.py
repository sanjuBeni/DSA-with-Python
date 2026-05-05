number = int(input('Enter a number: '))

"""
    Time Complexity is O(log10(n))
    Space complexity is O(1)code 
"""

def check_panlindrome(n):
    if n >= 0 and n <= 9:
        return True
    
    num = n
    new_num = 0
    while num > 0:
        mod = num % 10
        new_num = new_num * 10 + mod
        num = num // 10

    return new_num == n

print(check_panlindrome(number))