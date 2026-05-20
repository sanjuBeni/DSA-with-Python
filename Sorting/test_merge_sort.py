
# 1st merge two sorted list

a = [1, 2, 3]
b = [2, 3, 4, 5, 6, 7]

def merge_sorted_list(a:list, b:list)->list:
    if not a or not b:
        return []
    
    n, m = len(a), len(b)
    i = 0 
    j = 0 
    result = []
    while i < n and j < m:
        if a[i] < b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1
            
    if i < n:
        while i < n:
            result.append(a[i])
            i+=1
    if j < m:
        while j < m:
            result.append(b[j])
            j+=1

    return result

# print(merge_sorted_list(a, b))

nums = [4, 1, 7, 6, 3, 2, 8]

def sorting_list(nums:list)->list:
    if len(nums) <=1 :
        return nums
    
    mid = len(nums) // 2
    left_lst = nums[:mid]
    right_lst = nums[mid:]

    left = sorting_list(left_lst)
    right = sorting_list(right_lst)
    
    return merge_sorted_list(left, right)

print(sorting_list(nums))