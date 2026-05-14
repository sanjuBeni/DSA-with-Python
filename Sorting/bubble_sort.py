
nums = [5, 2, 1, 6, 9, 2, 4, 8]


"""
    TC: O(n^2)  => For average and wrost case
    SC: O(1)

    For best case if list is already sorted
    TC: O(n)  ==> See last method
"""

# Ascending Order
def ascending(nums):
    if not nums:
        return 0, []
    
    n = len(nums)
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

# ascending(nums)
# print(nums)

def decending(nums):
    if not nums:
        return 0, []
    
    n = len(nums)
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            if nums[j] < nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

# decending(nums)
# print(nums)

sorted_list = [1,2,3,4,5,6]
def best_case(nums):
    if nums:
        return 0, []
    
    n = len(nums)
    for i in range(n-2, -1, -1):
        is_sorted = True
        for j in range(i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_sorted = False

        if is_sorted:
            return
        
# best_case(sorted_list)