#State of the program right berfore the function call: q is an integer representing the position in the line (1 ≤ x < n ≤ 10^9), and x is an integer representing the number Vasya received during the settling (1 ≤ x < q).
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: Postcondition: `q` is an integer representing the position in the line (1 ≤ x < n ≤ 10^9), `x` is an integer representing the number Vasya received during the settling (1 ≤ x < q), `M` is a list containing `w`, where `w` is the square root of `q` and is an integer. If `w` is an integer and greater than or equal to `x - 1`, then `w` is added to the list `M`. Otherwise, the list `M` remains unchanged.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: The list M contains all divisors of q that are greater than or equal to x-1 and less than or equal to q/(x-1).
    return M
    #The program returns a list M that contains all divisors of q which are greater than or equal to x-1 and less than or equal to q/(x-1)
#Overall this is what the function does:The function accepts two parameters, `q` and `x`. `q` is an integer representing the position in the line (1 ≤ q < n ≤ 10^9), and `x` is an integer representing the number Vasya received during the settling (1 ≤ x < q). The function returns a list `M` that contains all divisors of `q` which are greater than or equal to `x-1` and less than or equal to `q/(x-1)`.

