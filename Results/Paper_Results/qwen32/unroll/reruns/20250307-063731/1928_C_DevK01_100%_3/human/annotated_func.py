#State of the program right berfore the function call: q and x are integers such that 1 ≤ x < q ≤ 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: `q` and `x` are integers such that 1 ≤ x < q ≤ 10^9. `M` is a list, and if `w` (the square root of `q`) is an integer and `w` is greater than or equal to `x - 1`, then `M` contains the integer `w`. Otherwise, `M` remains an empty list.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: `q` and `x` remain unchanged; `M` contains all divisors of `q` that are greater than or equal to `x - 1` and less than the integer square root of `q`; `i` is equal to the integer square root of `q`.
    return M
    #The program returns a list `M` containing all divisors of `q` that are greater than or equal to `x - 1` and less than the integer square root of `q`.
#Overall this is what the function does:The function accepts two integer parameters `q` and `x` such that 1 ≤ x < q ≤ 10^9. It returns a list `M` containing all divisors of `q` that are greater than or equal to `x - 1` and less than the integer square root of `q`.

