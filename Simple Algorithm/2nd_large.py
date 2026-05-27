nums = [55, 32, -97, 99, 3, 67]

# nums = [-10, -20, -50, -30, -5]
# nums = [155, 32, -97, 99, 3, 67]

"""
    TC: O(n)
    SC: O(1)
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

# print(find_2nd_large(nums))

def large_2nd(nums:list[int]):
    if not nums:
        return []
    
    first_large = float("-inf")
    second_large = float("-inf")
    for x in nums:
        if first_large < x:
            second_large = first_large
            first_large = x
        
        if second_large < x and first_large != x:
            second_large = x

    return second_large

print(large_2nd(nums))
        