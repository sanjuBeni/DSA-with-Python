"""
constraints

    1 <= n <= 10
    
    n can have 10^8

    m can have 10^8

    Solve both list and dict 
    Why use dict instead of list?
"""

n = [1, 4, 5, 7, 5, 9, 3, 4, 5, 9, 1]
m = [1, 2, 3, 4, 5, 66, 7, 88, 7, 55]

count_list = [0]*11

for num in n:
    count_list[num] += 1

for num in m:
    if num < 1 or num > 10:
        print(f"`{num}` count is: 0")
    else:
        print(f"`{num}` count is: {count_list[num]}")