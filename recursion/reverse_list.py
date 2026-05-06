
lst = [7, 5, 3, 1, 4, 8, 2, 9]
print(lst)

# TC : O(n/2) ~ O(n)
# SC : O(1)

def reverse_list(lst, right = 0, left = 0):
    if left > right:
        return
    
    lst[left], lst[right] = lst[right], lst[left]

    reverse_list(lst, right-1, left+1)

# reverse_list(lst, len(lst)-1)
# reverse_list(lst, 5, 2)
# print(lst)

left = 0
right = len(lst) - 1

while left < right:
    lst[left], lst[right] = lst[right], lst[left]
    left += 1
    right -= 1

print(lst)
