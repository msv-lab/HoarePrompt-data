#State of the program right berfore the function call: q is an integer such that 1 <= q <= 100, and for each of the q test cases, there are two integers n and x such that 1 <= x < n <= 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: `q` is an integer such that 1 <= `q` <= 100, `n` and `x` are integers for each of the `q` test cases with 1 <= `x` < `n` <= 10^9, `w` is the integer square root of `q`. If `w` is an integer and `w` is greater than or equal to `x - 1`, then `M` is a list containing the integer `w`. Otherwise, `M` remains an empty list.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: `M` contains the integer `w` if `w` is an integer and `w >= x - 1`, and all divisors `i` of `q` such that `1 <= i < w` and `i >= x - 1`, and all divisors `q // i` of `q` such that `1 <= i < w` and `q // i >= x - 1`.
    return M
    #The program returns a set `M` that contains the integer `w` if `w` is an integer and `w >= x - 1`, and all divisors `i` of `q` such that `1 <= i < w` and `i >= x - 1`, and all divisors `q // i` of `q` such that `1 <= i < w` and `q // i >= x - 1`.
#Overall this is what the function does:The function accepts an integer `q` and an integer `x`. It returns a list `M` containing the integer square root of `q` if it is an integer and greater than or equal to `x - 1`, along with all divisors `i` of `q` such that `1 <= i < w` and `i >= x - 1`, and all divisors `q // i` of `q` such that `1 <= i < w` and `q // i >= x - 1`.

