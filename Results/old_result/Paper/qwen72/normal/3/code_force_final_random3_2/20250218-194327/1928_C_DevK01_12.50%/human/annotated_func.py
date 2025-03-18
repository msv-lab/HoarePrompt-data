#State of the program right berfore the function call: q and x are integers such that 1 <= x < q <= 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: *`q` and `x` are integers such that 1 <= x < q <= 10^9, `M` is an empty list if `w` is not an integer or `w` is less than `x - 1`. If `w` is an integer and `w` is greater than or equal to `x - 1`, `M` is a list containing the integer `w`, and `w` is the square root of `q`.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: The loop has completed all iterations, `i` is equal to `int(w // 1)`, and `M` contains all integers `i` and `q // i` (where `i` is a divisor of `q` and `i` or `q // i` is greater than or equal to `x - 1`).
    return M
    #The program returns the list `M` which contains all integers `i` and `q // i` (where `i` is a divisor of `q` and both `i` and `q // i` are greater than or equal to `x - 1`).
#Overall this is what the function does:The function `func_1` accepts two integers `q` and `x` such that `1 <= x < q <= 10^9`. It returns a list `M` containing all divisors of `q` (including `q` itself) that are greater than or equal to `x - 1`. If `q` is a perfect square and its square root is greater than or equal to `x - 1`, the square root is also included in the list. The list `M` may be empty if no such divisors exist.

