#State of the program right berfore the function call: q and x are integers such that 1 ≤ x < q ≤ 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: q and x are integers such that 1 ≤ x < q ≤ 10^9, M is an empty list if w is not an integer or w < x - 1. If w is an integer and w ≥ x - 1, M is a list containing the integer w, where w is the square root of q.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: After all iterations of the loop, `q` and `x` remain integers such that \(1 \leq x < q \leq 10^9\). The variable `w` is the integer square root of `q`, and `i` is equal to `w`. The list `M` contains all integers `i` (from 1 to `w-1`) that are divisors of `q` and satisfy `i >= x - 1`, as well as their corresponding quotients `q // i` that also satisfy `q // i >= x - 1`.
    return M
    #The program returns the list `M` which contains all integers `i` from 1 to `w-1` that are divisors of `q` and satisfy `i >= x - 1`, along with their corresponding quotients `q // i` that also satisfy `q // i >= x - 1`. Here, `w` is the integer square root of `q`, and both `x` and `q` are integers such that \(1 \leq x < q \leq 10^9\).
#Overall this is what the function does:The function `func_1` accepts two integers `q` and `x` (where \(1 \leq x < q \leq 10^9\)) and returns a list `M` containing integers that are divisors of `q` and meet certain conditions. Specifically, `M` includes any integer `i` from 1 to the integer square root of `q` (denoted as `w`) that is a divisor of `q` and satisfies `i >= x - 1`, as well as the corresponding quotient `q // i` if it also satisfies `q // i >= x - 1`. If `w` itself is an integer and `w >= x - 1`, it is also included in `M`. The function ensures that the returned list `M` contains only valid divisors and their corresponding quotients that meet the specified criteria.

