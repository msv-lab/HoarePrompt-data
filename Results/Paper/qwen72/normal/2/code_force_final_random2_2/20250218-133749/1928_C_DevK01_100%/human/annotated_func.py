#State of the program right berfore the function call: q and x are integers such that 1 ≤ x < q ≤ 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: *q and x are integers such that 1 ≤ x < q ≤ 10^9, M is an empty list, and w is the square root of q. If w is an integer (i.e., w == w // 1) and w is greater than or equal to x - 1, then M is a list containing the integer value of the square root of q. Otherwise, M remains an empty list.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: The loop has completed all its iterations. `q` and `x` remain integers such that \(1 \leq x < q \leq 10^9\). `M` is a list containing the integer value of the square root of `q`, and all divisors of `q` that are greater than or equal to `x - 1` and their corresponding quotients (if the quotient is also greater than or equal to `x - 1`). `w` is the square root of `q`, and `i` is equal to `w` (the square root of `q`).
    return M
    #The program returns the list `M` which contains the integer value of the square root of `q` and all divisors of `q` that are greater than or equal to `x - 1` along with their corresponding quotients (if the quotient is also greater than or equal to `x - 1`).
#Overall this is what the function does:The function `func_1` accepts two parameters `q` and `x`, where both are integers and satisfy the condition 1 ≤ x < q ≤ 10^9. It returns a list `M` containing all divisors of `q` that are greater than or equal to `x - 1`, along with their corresponding quotients (if the quotient is also greater than or equal to `x - 1`). Additionally, if the square root of `q` is an integer and is greater than or equal to `x - 1`, it is also included in the list `M`.

