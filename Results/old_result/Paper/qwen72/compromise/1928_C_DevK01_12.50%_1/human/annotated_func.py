#State of the program right berfore the function call: q and x are integers such that 1 <= x < q <= 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: *`q` and `x` are integers such that 1 <= x < q <= 10^9, `M` is an empty list if `w` is not an integer or if `w` is less than `x - 1`. If `w` is an integer and `w` is greater than or equal to `x - 1`, `M` is a list containing the integer `w`, and `w` is the square root of `q`.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: `q` and `x` remain unchanged, `M` is a list containing all divisors of `q` that are greater than or equal to `x - 1`, and their corresponding complementary divisors (i.e., `q // i`), also greater than or equal to `x - 1`.
    return M
    #The program returns the list `M` containing all divisors of `q` that are greater than or equal to `x - 1`, along with their corresponding complementary divisors (i.e., `q // i`), also greater than or equal to `x - 1`.
#Overall this is what the function does:The function `func_1` accepts two integers, `q` and `x`, where `1 <= x < q <= 10^9`. It returns a list `M` containing all divisors of `q` that are greater than or equal to `x - 1`, along with their corresponding complementary divisors (i.e., `q // i`), also greater than or equal to `x - 1`. If the square root of `q` is an integer and is greater than or equal to `x - 1`, it is also included in the list `M`. The function does not modify the input parameters `q` and `x`.

