
x =  15
n = 4

def x_print_n_time(x, n):
    if n == 0:
        return
    
    print(x)
    x_print_n_time(x, n-1)

x_print_n_time(x, n)