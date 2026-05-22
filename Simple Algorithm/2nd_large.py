nums = [55, 32, -97, 99, 3, 67]

nums = [-10, -20, -50, -30, -5]
nums = [155, 32, -97, 99, 3, 67]

"""
    TC: 
    SC: 
"""


def find_2nd_large(nums:list):
    if not nums:
        return []
    
    first = second = float("-inf")
    for x in nums:
        if x > first:
            second = first
            first = x
        elif x > second and x != first:
            second = x

    return second

print(find_2nd_large(nums))
        