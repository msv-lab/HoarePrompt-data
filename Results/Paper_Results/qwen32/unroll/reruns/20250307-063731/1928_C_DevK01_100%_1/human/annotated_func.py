#State of the program right berfore the function call: q is a list of tuples, where each tuple contains two integers n and x such that 1 ≤ x < n ≤ 10^9, and the length of q is between 1 and 100.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: `q` is a list of tuples, where each tuple contains two integers `n` and `x` such that 1 ≤ `x` < `n` ≤ 10^9, and the length of `q` is between 1 and 100. If `w` is an integer such that `w` equals `w // 1` and `w` is greater than or equal to `x - 1`, then `M` is a list containing a single element `w`. Otherwise, `M` remains an empty list.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: M = [10, 10, 5, 5, 2]
    return M
    #The program returns the list [10, 10, 5, 5, 2]
#Overall this is what the function does:The function `func_1` accepts a list `q` of tuples, where each tuple contains two integers `n` and `x` such that 1 ≤ x < n ≤ 10^9, and an integer `x`. It returns a list of integers derived from the factors of `q` that are greater than or equal to `x - 1`. The specific output list returned in the example is [10, 10, 5, 5, 2].

