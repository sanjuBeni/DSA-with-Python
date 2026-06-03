
nums = [1, 2, 5, -7, 3, 10]

# result => [10, 1, 2, 5, -7, 3]

def right_rotate_one_place(nums:list):
    if not nums:
        return []
    
    l = len(nums)
    temp = nums[l-1]

    for i in range(l-2, -1, -1):
        nums[i+1] = nums[i]

    nums[0] = temp

# right_rotate_one_place(nums)

# print(nums)

# With Slicing
n = len(nums)
nums[:] = [nums[n-1]] + nums[0:n-1]
print(nums)