#State of the program right berfore the function call: q and x are integers such that 1 <= x < q <= 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: *`q` and `x` are integers such that 1 <= x < q <= 10^9, `M` is a list. If `w` is an integer and `w` >= `x - 1`, then `M` contains the integer `w`. Otherwise, `M` remains an empty list. `w` is the square root of `q`.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: `q` is an integer greater than 1, `w` is the square root of `q` and must be greater than or equal to `x - 1`, `i` is `int(w // 1)`. `M` is a list that contains all divisors of `q` that are greater than or equal to `x - 1` and their corresponding quotients `q // i` that are also greater than or equal to `x - 1`.
    return M
    #The program returns a list `M` that contains all divisors of `q` (an integer greater than 1) that are greater than or equal to `x - 1`, along with their corresponding quotients `q // i` that are also greater than or equal to `x - 1`.
#Overall this is what the function does:The function `func_1` accepts two integers `q` and `x` (where 1 <= x < q <= 10^9) and returns a list `M` containing all divisors of `q` that are greater than or equal to `x - 1`, along with their corresponding quotients `q // i` that are also greater than or equal to `x - 1`. If `q` is a perfect square and its square root is greater than or equal to `x - 1`, the square root is included in the list. The list `M` may be empty if no such divisors or quotients exist.

