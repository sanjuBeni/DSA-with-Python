
# 1 to N by head
n = 15
def by_head(n, i = 1):
    if n == 0:
        return
    print(i, end=" ")
    by_head(n - 1, i + 1)

# by_head(n)



# 1 to N by Tail
def by_tail(n):
    if n == 0:
        return 
    by_tail(n-1)
    print(n, end=" ")

# by_tail(n)

# N to 1 by Head
def n_to_1_by_head(n):
    if n == 0:
        return
    
    print(n, end=" ")
    n_to_1_by_head(n-1)

# n_to_1_by_head(n)

# N to 1 by Head
def n_to_1_by_tail(n, i = 1):
    if i > n:
        return
    n_to_1_by_tail(n, i + 1)
    print(i, end=" ")

n_to_1_by_tail(n)
