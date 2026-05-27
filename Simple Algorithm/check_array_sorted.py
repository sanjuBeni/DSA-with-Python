
# nums = [1, 2, 3, 4, 5, 6, 7]
nums = [1, 2, 3, 4, 5, 6, 7, 9, 8]

"""
    TC: O(n)
    SC: O(1)
"""

def is_list_sorted(nums:list[int])->bool:
    if not nums:
        return False
    
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
        
    return True

print(is_list_sorted(nums))