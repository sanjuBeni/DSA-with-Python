
nums = [4, 1, 7, 6, 3, 2, 8]

# TC: O(nlogn)  => best, avg case
# SC: O(1), Stack full

# TC: O(n^2)   => worst case  => [5, 5, 5, 5, 5, 5]

def partisan(nums:list, low:int, high:int):
    if not nums:
        return []
    
    pivot = nums[low]
    i = low
    j = high-1

    while i < j:
        while i <= high-1 and nums[i] < pivot:
            i+=1
        while j >= low+1 and nums[j] > pivot:
            j-=1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    # return nums
    return j


# print(partisan(nums, 0, len(nums)))

def quick_sort(nums, low, high):
    if low < high:
        p_idx = partisan(nums, low, high)

        quick_sort(nums, low, p_idx - 1)
        quick_sort(nums, p_idx + 1, high)

quick_sort(nums, 0, len(nums))
print(nums)