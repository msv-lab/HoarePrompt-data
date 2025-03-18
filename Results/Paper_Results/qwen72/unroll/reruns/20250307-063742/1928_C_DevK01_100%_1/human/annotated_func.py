#State of the program right berfore the function call: q and x are integers such that 1 <= x < q <= 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: *`q` and `x` are integers such that 1 <= x < q <= 10^9, `M` is an empty list if `w` is not an integer or `w` is less than `x - 1`. If `w` is an integer and `w` is greater than or equal to `x - 1`, `M` is a list containing the integer `w`, and `w` is the square root of `q`.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: `i = w` and `M` is a list containing all divisors of `q` that are greater than or equal to `x - 1` and their corresponding quotient pairs, excluding `w` if `w` is not an integer.
    return M
    #The program returns the list `M` which contains all divisors of `q` that are greater than or equal to `x - 1`, along with their corresponding quotient pairs, excluding `w` if `w` is not an integer.
#Overall this is what the function does:The function `func_1` accepts two integers `q` and `x` (1 <= x < q <= 10^9) and returns a list `M` containing all divisors of `q` that are greater than or equal to `x - 1`, along with their corresponding integer quotient pairs. If the square root of `q` is an integer and is greater than or equal to `x - 1`, it is included in the list `M`.

