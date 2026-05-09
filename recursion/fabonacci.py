
# Print 10 fabonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

def fab(num):
    if num < 0:
        return

    if num == 0 or num == 1:
        return  num
    
    return fab(num-1) + fab(num-2)

num = 11
# print(fab(num))

for i in range(num):
    print(fab(i), end=" ")