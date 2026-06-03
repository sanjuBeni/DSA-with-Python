
lst = [3, 9, 5, 6, 7, 3, 8]
k = 4

"""
    TC: O(n)
    SC: O(1)
"""

# def rotate_with_slice(nums:list, k:int):
#     if not nums:
#         return nums

#     n = len(nums)
#     if n < k:
#         return nums
#     nums[:] = nums[n-k:] + nums[: n-k]

# rotate_with_slice(lst, k)
# print(lst)

# def right_rotate_nth_place(nums: list, k: int):
#     if not nums:
#         return []
    
#     n = len(nums)
#     if n < k:
#         return nums
    
#     result = []
#     i = n - k
#     j = n - 1
#     while i <= j:    
#         result.append(nums[j])
#         j -= 1

#     print(result)

#     for i in range(n-k):
#         result.append(nums[i])

#     print(result)

# right_rotate_nth_place(lst, k)

"""
    With reverse list
"""
print(lst)
def reverse(nums:list, left:int, right:int):
    if not nums:
        return nums
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

n = len(lst)
reverse(lst, n-k, n-1)
reverse(lst, 0, n-k-1)
reverse(lst, 0, n-1)
print(lst)