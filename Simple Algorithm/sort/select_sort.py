
nums = [5, 7, 8, 4, 1, 6, 9, 2]

length = len(nums)

# Ascending 
# TC: O(n(n+1)/2)
# SC: O(1)
for i in range(0, length):
    min_index = i 
    for j in range(i+1, length):
        if nums[min_index] > nums[j] :
            min_index = j
    
    nums[i], nums[min_index] = nums[min_index], nums[i]

print(nums)

