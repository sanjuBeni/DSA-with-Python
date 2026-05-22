
nums = [55, 32, -97, 99, 3, 67]

nums = [-10, -20, -50, -30, -5]

"""
    TC: O(n) => O(n/2)
    SC: O(1)
"""


def find_largest_num(nums:list):
    if not nums:
        return []
    
    # large = nums[0]
    large = float("-inf")

    i = 0
    j = len(nums) -1

    while i < j:
        large = max(large, nums[i])    
        large = max(large, nums[j])
        # if large < nums[i]:
        #     large = nums[i]
        
        # if large < nums[j]:
        #     large = nums[j]
        i += 1
        j -= 1

    return large    


print(find_largest_num(nums))