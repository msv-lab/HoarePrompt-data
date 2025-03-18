#State of the program right berfore the function call: q and x are integers such that 1 \leq x < q \leq 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: *`q` and `x` are integers such that 1 ≤ x < q ≤ 10^9, `M` is a list. If `w` (the square root of `q`) is an integer and `w` is greater than or equal to `x - 1`, then `M` contains `[w]`. Otherwise, `M` remains an empty list.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: `q` and `x` are integers such that 1 ≤ x < q ≤ 10^9, `w` (the square root of `q`) is an integer and `w` is greater than or equal to `x - 1`, `i` is `int(w // 1)`, and `M` contains all divisors of `q` that are greater than or equal to `x - 1`, as well as their corresponding quotients `q // d` that are also greater than or equal to `x - 1`.
    return M
    #The program returns a list `M` that contains all divisors of `q` that are greater than or equal to `x - 1`, as well as their corresponding quotients `q // d` that are also greater than or equal to `x - 1`.
#Overall this is what the function does:The function `func_1` accepts two integers `q` and `x` (where 1 ≤ x < q ≤ 10^9) and returns a list `M` containing all divisors of `q` that are greater than or equal to `x - 1`, as well as their corresponding quotients `q // d` that are also greater than or equal to `x - 1`. If the square root of `q` is an integer and is greater than or equal to `x - 1`, it is also included in the list `M`.

