#State of the program right berfore the function call: q and x are integers such that 1 <= x < q <= 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: *`q` and `x` are integers such that 1 <= x < q <= 10^9, `M` is a list. If `w` is an integer and `w` >= `x - 1`, `M` contains the integer `w`, which is the square root of `q`. Otherwise, `M` remains an empty list.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: `q` and `x` remain unchanged, `M` contains integers that are divisors of `q` and are greater than or equal to `x - 1`.
    return M
    #The program returns the list `M` which contains integers that are divisors of `q` and are greater than or equal to `x - 1`.
#Overall this is what the function does:The function `func_1` accepts two integers `q` and `x` (where 1 <= x < q <= 10^9) and returns a list `M` containing all divisors of `q` that are greater than or equal to `x - 1`. If the square root of `q` is an integer and is greater than or equal to `x - 1`, it is also included in the list `M`. The function does not modify the input variables `q` and `x`.

