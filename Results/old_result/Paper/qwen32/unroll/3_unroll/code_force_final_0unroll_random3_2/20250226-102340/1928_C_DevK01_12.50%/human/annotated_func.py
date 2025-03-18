#State of the program right berfore the function call: q is a list of tuples, where each tuple contains two integers n and x such that 1 ≤ x < n ≤ 10^9, and q contains between 1 and 100 tuples.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: The program raises a TypeError because `math.sqrt()` is called with a list instead of a number. `q` is a list of tuples, where each tuple contains two integers `n` and `x` such that 1 ≤ `x` < `n` ≤ 10^9, and `q` contains between 1 and 100 tuples. If `w` is an integer and `w` is greater than or equal to `x - 1`, then `M` is a list containing the integer `w`. Otherwise, `M` remains an empty list.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: M is a list containing the divisors of n that meet the conditions.
    return M
    #The program returns list M, which contains the divisors of n that meet the conditions.
#Overall this is what the function does:The function accepts a list of tuples `q`, where each tuple contains two integers `n` and `x` such that 1 ≤ `x` < `n` ≤ 10^9, and an integer `x`. It returns a list `M` containing the divisors of `n` from each tuple in `q` that are greater than or equal to `x`. However, due to an error in the code, the function will raise a `TypeError` when attempting to compute the square root of `q`, which is a list instead of a number.

