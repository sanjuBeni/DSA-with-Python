"""
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
"""

# Write a fibonacci serice from 0 to 21
# fabo = [0,1]
# pre_index = 0
# pre_next_index = 1
# while fabo[len(fabo) - 1] < 21:
#     new_num = fabo[pre_index] + fabo[pre_next_index]
#     fabo.append(new_num)
#     pre_index += 1
#     pre_next_index += 1

# print(fabo)

"""
    nth fabonacci number
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

    f(5) = f(5-1) + f(5-2) => 3+2 => 5
    f(6) = f(6-1) + f(6-2) => 5+3 => 8
    f(7) = f(7-1) + f(7-2) => 8+5 => 13

    f(n-1) + f(n-2)
"""

def find_fabonacci(num):
    if num == 0 or num == 1:
        return num
    return find_fabonacci(num-1) + find_fabonacci(num-2)

print(find_fabonacci(5))
print(find_fabonacci(6))
print(find_fabonacci(7))