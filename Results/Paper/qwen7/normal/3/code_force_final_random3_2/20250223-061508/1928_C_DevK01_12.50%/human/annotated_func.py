#State of the program right berfore the function call: q is an integer representing the position Vasya occupied in the line, and x is an integer representing the number Vasya received during the settling. Both q and x satisfy 1 <= x < q <= 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: `q` is an integer representing Vasya's position in the line, `x` is an integer representing the number Vasya received during the settling, `w` is the square root of `q`, and `M` is a list containing `[w]` if `w` is an integer and `w >= x - 1`. Otherwise, `M` remains unchanged.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: `q` is an integer, `x` is an integer, `w` is the square root of `q` and must be an integer and `w >= x - 1`, `M` is a list containing all divisors of `q` that are greater than or equal to `x - 1` and their corresponding quotients when divided into `q`.
    return M
    #The program returns a list `M` containing all divisors of `q` that are greater than or equal to `x - 1` and their corresponding quotients when divided into `q`.
#Overall this is what the function does:The function accepts two parameters, `q` and `x`, where `q` is an integer representing Vasya's position in the line, and `x` is an integer representing the number Vasya received during the settling. Both `q` and `x` satisfy 1 <= x < q <= 10^9. The function calculates and returns a list `M` containing all divisors of `q` that are greater than or equal to `x - 1` and their corresponding quotients when divided into `q`.

