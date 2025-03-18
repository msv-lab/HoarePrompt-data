#State of the program right berfore the function call: q is an integer representing the position in the line (1 <= x < n <= 10^9), and x is an integer representing the number Vasya received during the settling (1 <= x < q).
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: Postcondition: `q` is an integer representing the position in the line (1 <= x < n <= 10^9), `x` is an integer representing the number Vasya received during the settling (1 <= x < q), `M` is a list containing the square root of `q`, `w` is the square root of `q`, and if `w` is an integer and greater than or equal to `x - 1`, then `w` remains unchanged; otherwise, `M` and `w` remain as initially defined.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: The value of `M` is a list of divisors of `q` that are greater than or equal to `x-1`.
    return M
    #The program returns a list `M` of divisors of `q` that are greater than or equal to `x-1`
#Overall this is what the function does:The function accepts two parameters, `q` and `x`. `q` represents the position in the line, and `x` represents the number Vasya received during the settling. The function calculates and returns a list `M` containing all divisors of `q` that are greater than or equal to `x-1`. If `w` (the square root of `q`) is an integer and greater than or equal to `x-1`, `w` is included in the list `M`. The function iterates through all numbers less than the square root of `q` to find other divisors that meet the condition and adds them to the list `M`.

