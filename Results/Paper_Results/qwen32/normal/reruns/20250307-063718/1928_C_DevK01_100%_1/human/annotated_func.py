#State of the program right berfore the function call: q is a list of tuples, where each tuple contains two integers n and x such that 1 ≤ x < n ≤ 10^9, and q contains between 1 and 100 tuples.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: `q` is a list of tuples, where each tuple contains two integers `n` and `x` such that 1 ≤ `x` < `n` ≤ 10^9, and `q` contains between 1 and 100 tuples. If `w` is an integer and `w` is greater than or equal to `x - 1`, then `M` is a list containing the integer `w`. Otherwise, `M` remains an empty list.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: `M` contains all divisors `i` and `q // i` of `q` such that `i` and `q // i` are greater than or equal to `x - 1` and `i` ranges from 1 to `w - 1`.
    return M
    #The program returns a list `M` containing all divisors `i` and `q // i` of `q` such that `i` and `q // i` are greater than or equal to `x - 1` and `i` ranges from 1 to `w - 1`.
#Overall this is what the function does:The function `func_1` accepts a list `q` of tuples, where each tuple contains two integers `n` and `x` such that 1 ≤ x < n ≤ 10^9, and `q` contains between 1 and 100 tuples. The function returns a list `M` containing all divisors `i` and `n // i` of `n` such that `i` and `n // i` are greater than or equal to `x - 1` and `i` ranges from 1 to `sqrt(n) - 1`.

