#State of the program right berfore the function call: q is an integer representing the position in the line (1 ≤ x < n ≤ 10^9), and x is an integer representing the number Vasya received during the settling (1 ≤ x < q).
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: Postcondition: `q` is an integer representing the position in the line (1 ≤ x < n ≤ 10^9), `x` is an integer representing the number Vasya received during the settling (1 ≤ x < q), `M` is a list containing one element which is `w` if `w` is an integer and greater than or equal to `x - 1`, and `w` is the square root of `q`.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: Output State: `i` is equal to `w`, `q` is an integer representing the position in the line (1 ≤ q < n ≤ 10^9), `x` is an integer representing the number Vasya received during the settling (1 ≤ x < q), `M` is a list containing all integers `j` such that `x - 1 ≤ j < w` and `q % j == 0` or `q // j ≥ x - 1`.
    #
    #This means that after the loop has executed all its iterations, `i` will be equal to `w`, as the loop continues to increment `i` until it reaches `w`. The list `M` will contain all integers `j` between `x - 1` and `w - 1` (inclusive) that either divide `q` exactly (`q % j == 0`) or whose corresponding quotient `q // j` is greater than or equal to `x - 1`.
    return M
    #The program returns a list `M` containing all integers `j` such that `x - 1 ≤ j < w` and either `q % j == 0` or `q // j ≥ x - 1`
#Overall this is what the function does:The function `func_1` accepts two parameters, `q` and `x`, where `q` represents the position in a line and `x` is an integer Vasya received. It returns a list `M` containing all integers `j` such that `x - 1 ≤ j < w` and either `q % j == 0` or `q // j ≥ x - 1`, where `w` is the integer part of the square root of `q`.

