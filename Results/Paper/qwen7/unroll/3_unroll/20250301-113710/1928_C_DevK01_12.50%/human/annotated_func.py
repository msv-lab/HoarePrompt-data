#State of the program right berfore the function call: q is an integer representing the number of test cases, and for each test case, x and n are integers such that 1 ≤ x < n ≤ 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: Postcondition: `q` is an integer representing the number of test cases, `w` is the square root of `q` and is an integer greater than or equal to `x - 1`, `x` and `n` are integers such that 1 ≤ `x` < `n` ≤ 10^9, `M` is a list containing one element which is `w`.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: `q` is an integer representing the number of test cases, `w` is the integer square root of `q` and is greater than or equal to `x - 1`, `x` and `n` are integers such that 1 ≤ `x` < `n` ≤ 10^9, `M` is a list containing all divisors of `q` that are greater than or equal to `x - 1`.
    return M
    #The program returns a list `M` containing all divisors of `q` that are greater than or equal to `x - 1`
#Overall this is what the function does:The function accepts two parameters, `q` (an integer) and `x` (an integer). It calculates the integer square root of `q` and stores it in `w`. If `w` is greater than or equal to `x - 1`, it adds `w` to the list `M`. Then, it iterates through all integers from 1 to `w` (excluding `w` itself), checking if they are divisors of `q` and adding them to `M` if they are greater than or equal to `x - 1`. Finally, it returns the list `M` containing all divisors of `q` that are greater than or equal to `x - 1`.

