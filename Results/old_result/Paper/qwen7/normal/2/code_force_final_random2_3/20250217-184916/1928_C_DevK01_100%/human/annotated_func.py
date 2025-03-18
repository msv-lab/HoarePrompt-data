#State of the program right berfore the function call: q is an integer representing the position in the line (1 <= x < n <= 10^9), and x is an integer representing the number Vasya received during the settling (1 <= x < q).
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: Postcondition: `q` is an integer representing the position in the line (1 <= x < n <= 10^9), and `x` is an integer representing the number Vasya received during the settling (1 <= x < q); `M` is a list. If `w` (the square root of `q`) is an integer and `w` is greater than or equal to `x - 1`, then `M` contains `[w]`. Otherwise, `M` remains unchanged.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: Output State: `i` will be `w + 1`, `q` must be a perfect square greater than 1, `w` (the square root of `q`) is an integer, and `M` will contain all integers from 1 up to and including `w`.
    #
    #Explanation: The loop continues to increment `i` until it reaches `w + 1`. During each iteration, if `i` is greater than or equal to `x - 1`, `i` itself or `q // i` is added to the list `M`. Since the loop processes all divisors of `q` up to `w`, `M` will include all integers from 1 up to and including `w`.
    return M
    #The program returns a list `M` containing all integers from 1 up to and including the square root `w` of `q`, where `q` is a perfect square greater than 1 and `w` is an integer.
#Overall this is what the function does:The function accepts two parameters, `q` and `x`. It returns a list `M` containing all integers from 1 up to and including the square root `w` of `q`, where `q` is a perfect square greater than 1 and `w` is an integer. If the square root `w` of `q` is an integer and is greater than or equal to `x - 1`, then `w` is included in the list `M`. The function iterates through all divisors of `q` up to `w`, adding those that meet the condition to the list `M`.

