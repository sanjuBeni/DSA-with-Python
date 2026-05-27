
nums = [1, 1, 1, 2, 3, 4, 4, 7, 9, 9, 9, 10]


"""
    TC: O(N)
    SC: O(N), bcz dictionary if full
"""

def remove_duplicate(nums:list)->list:
    if not nums:
        return []
    
    dic = {}
    i = 0
    for x in nums:
        if x not in dic:
            dic[x] = 0
            nums[i] = x
            i += 1

    # data = list(dic.keys())
    # for i in range(len(data)):
    #     nums[i] = data[i]

    # print(dic)
    print(i)
    return nums

# print(remove_duplicate(nums))

def total_duplicate(nums:list):
    if not nums:
        return 0
    
    n = len(nums)
    if n == 1:
        return 1
    i = 0
    j = i+1
    while j < n:
        # if nums[i] != nums[j] and nums[j] not in nums[:i+1]:
        if nums[j] not in nums[:i+1]:
            i+=1
            nums[i], nums[j] = nums[j], nums[i]

        j+=1

    return i+1

print(total_duplicate(nums), nums)
    