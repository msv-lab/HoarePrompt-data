#State of the program right berfore the function call: q and x are integers such that 1 ≤ x < q ≤ 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: *q and x are integers such that 1 ≤ x < q ≤ 10^9, M is an empty list, and w is the square root of q. If w is an integer (i.e., w == w // 1) and w is greater than or equal to x - 1, then M contains the integer value of w. Otherwise, M remains an empty list.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: After all iterations, `q` and `x` are integers such that \(1 \leq x < q \leq 10^9\), `w` is the square root of `q`, `i` is equal to `w`, and `M` contains all divisors of `q` that are greater than or equal to `x - 1`, including both the divisor and its corresponding quotient if the quotient is also greater than or equal to `x - 1`.
    return M
    #The program returns `M`, which is a list containing all divisors of `q` that are greater than or equal to `x - 1`, including both the divisor and its corresponding quotient if the quotient is also greater than or equal to `x - 1`. Here, `q` is an integer between 1 and \(10^9\), and `x` is an integer such that \(1 \leq x < q\). The variable `w` is the square root of `q`, and `i` is equal to `w`.
#Overall this is what the function does:The function `func_1` accepts two parameters, `q` and `x`, where `q` is an integer between 1 and \(10^9\) and `x` is an integer such that \(1 \leq x < q\). It returns a list `M` containing all divisors of `q` that are greater than or equal to `x - 1`, including both the divisor and its corresponding quotient if the quotient is also greater than or equal to `x - 1`. If the square root of `q` is an integer and is greater than or equal to `x - 1`, it is also included in the list `M`.

