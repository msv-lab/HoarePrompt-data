#State of the program right berfore the function call: q is a list of tuples where each tuple contains two integers (n, x) representing Vasya's position in the line and the number Vasya received during the settling, respectively, with the constraints 1 ≤ x < n ≤ 10^9. The length of q is between 1 and 100, inclusive.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: q is a list of tuples where each tuple contains two integers (n, x) representing Vasya's position in the line and the number Vasya received during the settling, respectively, with the constraints 1 ≤ x < n ≤ 10^9. The length of q is between 1 and 100, inclusive. If w is an integer such that w is equal to its integer division by 1 and w is greater than or equal to x - 1, then M is a list containing the single element w. Otherwise, M remains an empty list.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: `M` contains all divisors of `q` that are greater than or equal to `x - 1` and their corresponding quotients if they are also greater than or equal to `x - 1`. `i` is equal to the length of `q`.
    return M
    #The program returns `M`, which contains all divisors of `q` that are greater than or equal to `x - 1` along with their corresponding quotients if those quotients are also greater than or equal to `x - 1`.
#Overall this is what the function does:The function `func_1` accepts a list of tuples `q` where each tuple contains two integers `(n, x)` representing Vasya's position in the line and the number Vasya received during the settling, respectively, with the constraints \(1 \leq x < n \leq 10^9\). It also accepts an integer `x`. The function returns a list `M` containing all divisors of `n` from each tuple in `q` that are greater than or equal to `x - 1`, along with their corresponding quotients if those quotients are also greater than or equal to `x - 1`.

