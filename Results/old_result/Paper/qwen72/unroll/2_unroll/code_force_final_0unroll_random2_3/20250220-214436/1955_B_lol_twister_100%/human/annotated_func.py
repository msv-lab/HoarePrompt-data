#State of the program right berfore the function call: n is an integer such that 2 <= n <= 500, c and d are integers such that 1 <= c, d <= 10^6, and l is a list of n^2 integers such that 1 <= l[i] <= 10^9 for all 0 <= i < n^2.
def func_1(n, c, d, l):
    a = min(l)
    li = []
    for k in range(0, n):
        for h in range(0, n):
            li.append(a + k * c + d * h)
        
    #State: `n` is an integer such that 2 <= n <= 500, `c` and `d` are integers such that 1 <= c, d <= 10^6, `l` is a list of n^2 integers such that 1 <= l[i] <= 10^9 for all 0 <= i < n^2, `a` is the minimum value in the list `l`, `li` is a list of n^2 integers where each element is calculated as `a + k * c + d * h` for 0 <= k, h < n.
    li.sort()
    l.sort()
    if (l == li) :
        return 'yes'
        #The program returns 'yes'
    #State: `n` is an integer such that 2 <= n <= 500, `c` and `d` are integers such that 1 <= c, d <= 10^6, `l` is a sorted list of n^2 integers in ascending order, `a` is the minimum value in the list `l`, `li` is a sorted list of n^2 integers where each element is calculated as `a + k * c + d * h` for 0 <= k, h < n, and `l` is not equal to `li`.
    return 'no'
    #The program returns the string 'no'.
#Overall this is what the function does:The function `func_1` takes four parameters: `n`, `c`, `d`, and `l`. It returns 'yes' if the sorted list `l` matches a newly generated and sorted list `li`, where each element in `li` is calculated as `a + k * c + d * h` for `0 <= k, h < n`, with `a` being the minimum value in the original list `l`. Otherwise, it returns 'no'. The function does not modify the input parameters.

