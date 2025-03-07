#State of the program right berfore the function call: q is a list of tuples, where each tuple contains two integers n and x such that 1 ≤ x < n ≤ 10^9, and q contains between 1 and 100 tuples.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: `q` is a list of tuples, where each tuple contains two integers `n` and `x` such that 1 ≤ `x` < `n` ≤ 10^9, and `q` contains between 1 and 100 tuples. If `w` is an integer that satisfies `w == w // 1` and `w >= x - 1`, then `M` is a list containing the single element `w`. Otherwise, `M` remains an empty list.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: `i` equals `w`, and `M` contains all valid divisors of `q` that satisfy the conditions `i >= x - 1` and `q // i >= x - 1` for each tuple `(n, x)` in `q`.
    return M
    #The program returns M, which contains all valid divisors of q that satisfy the conditions i >= x - 1 and q // i >= x - 1 for each tuple (n, x) in q.
#Overall this is what the function does:The function accepts a list `q` of tuples, where each tuple contains two integers `n` and `x` such that 1 ≤ x < n ≤ 10^9, and `q` contains between 1 and 100 tuples. It returns a list `M` containing all valid divisors of `n` from each tuple `(n, x)` in `q` that satisfy the conditions `i >= x - 1` and `n // i >= x - 1`.

