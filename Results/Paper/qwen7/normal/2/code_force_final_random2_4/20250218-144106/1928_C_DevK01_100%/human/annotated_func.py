#State of the program right berfore the function call: q is an integer representing the position Vasya occupied in the line, and x is an integer representing the number Vasya received during the settling. Both q and x satisfy 1 ≤ x < q ≤ 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: Postcondition: `q` is an integer representing the position Vasya occupied in the line, `x` is an integer representing the number Vasya received during the settling, `w` is the square root of `q`, the list `M` contains the element `w`, and either `w` is an integer and is greater than or equal to `x - 1`, or there is no else part in the code.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: Output State: `i` is greater than or equal to `w`, `q` is an integer representing the position Vasya occupied in the line, `x` is an integer representing the number Vasya received during the settling, `w` is the square root of `q` and must be greater than or equal to 2, the list `M` contains the elements `w` and all integers `i` from 2 to `w` (inclusive) that satisfy the conditions inside the loop, and if `q` is divisible by `i` and `q // i` is greater than or equal to `x - 1`, then `M` also contains `q // i`.
    #
    #This means that after the loop has executed all its iterations, `i` will be set to the next integer greater than `w`, indicating that the loop has completed all its iterations. The list `M` will contain `w` and all integers from 2 to `w` that divide `q` and meet the specified conditions, along with any additional divisors of `q` that are greater than or equal to `x - 1`.
    return M
    #The program returns a list `M` containing `w` and all integers from 2 to `w` that divide `q` and meet the specified conditions, along with any additional divisors of `q` that are greater than or equal to `x - 1`.
#Overall this is what the function does:The function accepts two parameters, `q` (an integer representing Vasya's position in the line) and `x` (an integer representing the number Vasya received). It calculates the square root of `q` and checks for divisors of `q` within the range from 2 to the square root of `q`. If a divisor meets certain conditions (specifically, being greater than or equal to `x - 1`), it is added to the list `M`. Finally, the function returns the list `M` containing these divisors.

