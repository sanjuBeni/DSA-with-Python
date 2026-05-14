
"""
    Merge 2 sorted list 
    TC: O(nlogn)
    SC: O(n) ==> Stack space
"""
l1 = [1, 2, 3, 4]
l2 = [1, 3, 5, 6, 7, 8, 9]

def merge_2_sorted_list(list1:list, list2:list)->list:
    if not list1 or not list2:
        return []
    len_l1, len_l2 = len(list1), len(list2)
    i = 0
    j = 0
    result = []
    while i < len_l1 and j < len_l2:
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    if len_l1 > i:
        while len_l1 > i:
            result.append(list1[i])
            i += 1

    if len_l2 > j :
        while len_l2 > j:
            result.append(list2[j])
            j += 1
    return result


# print(merge_2_sorted_list(l1, l2))


"""
    Sorted list with merge technic
"""
lst = [5, 4, 1, 9, 8, 7, 2, 3, 10]

def sort_list_with_merge(lst:list)->list:
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst [mid:]

    left_half = sort_list_with_merge(left_half)
    right_half = sort_list_with_merge(right_half)

    return merge_2_sorted_list(left_half, right_half)

print(lst)
print(sort_list_with_merge(lst))