#State of the program right berfore the function call: q is an integer representing Vasya's position in the line, and x is an integer representing the number Vasya received during the settling, such that 1 <= x < q <= 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: *`q` is an integer representing Vasya's position in the line, `x` is an integer representing the number Vasya received during the settling, such that 1 <= x < q <= 10^9, `w` is the square root of `q`, and `M` is a list. If `w` is an integer (i.e., `q` is a perfect square) and `w` is greater than or equal to `x - 1`, then `M` contains the integer `w`. Otherwise, `M` remains an empty list.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: `i` is equal to `w`, `M` contains all divisors of `q` that are greater than or equal to `x - 1`, and their corresponding quotient pairs that are also greater than or equal to `x - 1`. The values of `q`, `x`, and `w` remain unchanged.
    return M
    #The program returns `M`, which contains all divisors of `q` that are greater than or equal to `x - 1`, along with their corresponding quotient pairs that are also greater than or equal to `x - 1`. The values of `q`, `x`, and `w` remain unchanged.
#Overall this is what the function does:The function `func_1` accepts two integers, `q` and `x`, and returns a list `M` containing all divisors of `q` that are greater than or equal to `x - 1`, along with their corresponding quotient pairs that are also greater than or equal to `x - 1`. The values of `q` and `x` remain unchanged. If `q` is a perfect square and its square root is greater than or equal to `x - 1`, the square root is also included in the list `M`.

