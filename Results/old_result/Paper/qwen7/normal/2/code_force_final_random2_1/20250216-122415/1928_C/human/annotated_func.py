#State of the program right berfore the function call: q is an integer representing the position in the line (1 ≤ x < n ≤ 10^9), and x is an integer representing the number Vasya received during the settling (1 ≤ x < n).
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: `q` is an integer representing the position in the line (1 ≤ q < n ≤ 10^9), and `x` is an integer representing the number Vasya received during the settling (1 ≤ x < n); `M` is a list containing `[w]`; `w` is the square root of `q` and is an integer greater than or equal to `x - 1`.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: Output State: `i` is `w`, `q` is an integer representing the position in the line (1 ≤ q < n ≤ 10^9), `x` is an integer representing the number Vasya received during the settling (1 ≤ x < n), `w` is the square root of `q` and is an integer greater than or equal to `x - 1`, and `M` is a list containing all divisors of `q` that are greater than or equal to `x - 1`.
    #
    #Explanation: The loop continues to increment `i` until it reaches `w`. During each iteration, it checks if `q` is divisible by `i`. If `i` is greater than or equal to `x - 1`, it adds `i` to the list `M`. Similarly, if `q // i` is greater than or equal to `x - 1`, it adds `q // i` to the list `M`. After executing the loop, `i` will be equal to `w`, and `M` will contain all divisors of `q` that meet the specified condition.
    return M
    #The program returns a list `M` containing all divisors of `q` that are greater than or equal to `x - 1`
#Overall this is what the function does:The function accepts two parameters, `q` and `x`. `q` represents the position in the line, and `x` represents the number Vasya received during the settling. The function calculates all divisors of `q` that are greater than or equal to `x - 1` and returns them as a list `M`.

