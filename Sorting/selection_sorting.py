
# List ascending and descending

# 5, 10, 20, 12
lst = [9, 5, 7, 1, 3, 5, 10, 20, 12]

def ascending_order(lst):
    if not lst:
        return 0, []
    
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j

        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    return lst

print(ascending_order(lst))

def decending_order(lst):
    if not lst:
        return 0, []
    
    for i in range(len(lst)):
        max_idx = i
        for j in range(i+1, len(lst)):
            if lst[max_idx] < lst[j]:
                max_idx = j

        lst[i], lst[max_idx] = lst[max_idx], lst[i]

    return lst
    
print(decending_order(lst))