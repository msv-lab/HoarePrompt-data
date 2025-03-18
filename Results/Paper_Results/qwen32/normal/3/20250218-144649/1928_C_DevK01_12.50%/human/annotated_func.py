#State of the program right berfore the function call: q is a list of tuples, where each tuple contains two integers n and x, such that 1 ≤ x < n ≤ 10^9, and q contains between 1 and 100 tuples.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: `q` is a list of tuples, where each tuple contains two integers `n` and `x`, such that 1 ≤ x < n ≤ 10^9, and `q` contains between 1 and 100 tuples. `M` is a list that contains the integer `w` if `w` is an integer and `w >= x - 1`. If `w` does not satisfy these conditions, `M` remains an empty list.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: `q` is a list of tuples, where each tuple contains two integers `n` and `x`, such that 1 ≤ x < n ≤ 10^9, and `q` contains between 1 and 100 tuples. `M` is a list containing the integer `w` and all integers `i` and `n // i` such that `i >= x - 1` and `n // i >= x - 1` for all `i` from 1 to `w - 1` and for all tuples `(n, x)` in `q`.
    return M
    #The program returns a list `M` that contains the integer `w` (the maximum `n` from all tuples in `q`), and for each tuple `(n, x)` in `q`, it includes all integers `i` and `n // i` such that `i >= x - 1` and `n // i >= x - 1`.
#Overall this is what the function does:The function accepts a list `q` of tuples, where each tuple contains two integers `n` and `x` with the constraints 1 ≤ x < n ≤ 10^9, and `q` contains between 1 and 100 tuples. The function returns a list `M` that includes the integer `w` (the square root of the maximum `n` from all tuples in `q` if `w` is an integer and `w >= x - 1` for any tuple). For each tuple `(n, x)` in `q`, the function includes all integers `i` and `n // i` in the list `M` such that both `i` and `n // i` are greater than or equal to `x - 1`.

