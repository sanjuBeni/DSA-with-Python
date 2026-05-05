nums = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]

# How many times digit comes in list

"""
    TC is O(n)
    SC is also O(n), bcz in wrost case every digit only one time came
"""
def count_digit_in_list(nums):
    if len(nums) <= 0:
        return 'List is empty'
    
    freq_map = {}
    for i in range(len(nums)): # TC : O(n)
        # if nums[i] in freq_map: # TC of finding key in dictionary is O(1)
        #     freq_map[nums[i]] = freq_map[nums[i]] + 1 # TC of adding value in key is O(1)
        # else:
        #     freq_map[nums[i]] = 1 # TC of adding value in key is O(1)
        freq_map[nums[i]] = freq_map.get(nums[i], 0) + 1

    return freq_map

print(count_digit_in_list(nums=nums))