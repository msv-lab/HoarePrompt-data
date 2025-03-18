#State of the program right berfore the function call: q is an integer representing the number of test cases such that 1 <= q <= 100, and for each test case, there are two integers n and x where 1 <= x < n <= 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: `q` is an integer representing the number of test cases such that 1 <= q <= 100, `w` is the square root of `q` and `w` is an integer (i.e., `w == w // 1`) if and only if `w` is greater than or equal to `x - 1`, and `M` is a list containing the single element `w` if the condition is true. Otherwise, `M` remains an empty list.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: `q` is an integer, `w` is the integer square root of `q`, and `M` is a list containing `w` (if `w >= x - 1`) and all divisors of `q` and their corresponding quotients that are greater than or equal to `x - 1`.
    return M
    #The program returns a list `M` that contains the integer square root `w` of `q` if `w >= x - 1`, and all divisors of `q` along with their corresponding quotients that are greater than or equal to `x - 1`.
#Overall this is what the function does:The function accepts two parameters: `q` (an integer) and `x` (an integer). It calculates the integer square root `w` of `q` and checks if `w` is greater than or equal to `x - 1`. If true, `w` is added to a list `M`. The function then finds all divisors of `q` and their corresponding quotients that are greater than or equal to `x - 1` and adds them to `M`. Finally, the function returns the list `M`.

