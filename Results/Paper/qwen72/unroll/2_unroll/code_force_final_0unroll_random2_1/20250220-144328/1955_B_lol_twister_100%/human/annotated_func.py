#State of the program right berfore the function call: n is an integer such that 2 <= n <= 500, c and d are integers such that 1 <= c, d <= 10^6, and l is a list of n^2 integers where 1 <= b_i <= 10^9.
def func_1(n, c, d, l):
    a = min(l)
    li = []
    for k in range(0, n):
        for h in range(0, n):
            li.append(a + k * c + d * h)
        
    #State: `n` is an integer such that 2 <= n <= 500, `c` and `d` are integers such that 1 <= c, d <= 10^6, `l` is a list of n^2 integers where 1 <= b_i <= 10^9, `a` is the smallest integer in the list `l`, `li` is a list of n^2 integers where each integer is of the form `a + k * c + d * h` for 0 <= k < n and 0 <= h < n.
    li.sort()
    l.sort()
    if (l == li) :
        return 'yes'
        #The program returns 'yes'
    #State: `n` is an integer such that 2 <= n <= 500, `c` and `d` are integers such that 1 <= c, d <= 10^6, `l` is a sorted list of `n^2` integers where 1 <= b_i <= 10^9, `a` is the smallest integer in the list `l`, `li` is a sorted list of `n^2` integers where each integer is of the form `a + k * c + d * h` for 0 <= k < n and 0 <= h < n, and `l` is not equal to `li`.
    return 'no'
    #The program returns 'no'.
#Overall this is what the function does:The function `func_1` accepts four parameters: `n`, `c`, `d`, and `l`. `n` is an integer such that 2 <= n <= 500, `c` and `d` are integers such that 1 <= c, d <= 10^6, and `l` is a list of `n^2` integers where each integer is between 1 and 10^9. The function generates a new list `li` containing `n^2` integers, where each integer is of the form `a + k * c + d * h` for 0 <= k < n and 0 <= h < n, with `a` being the smallest integer in `l`. It then sorts both `l` and `li`. If the sorted list `l` is equal to the sorted list `li`, the function returns 'yes'. Otherwise, it returns 'no'.

