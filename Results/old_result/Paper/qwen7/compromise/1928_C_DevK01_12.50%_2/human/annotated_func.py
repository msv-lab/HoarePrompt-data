#State of the program right berfore the function call: q is an integer representing the number of test cases where 1 ≤ q ≤ 100, and for each test case, x and n are integers such that 1 ≤ x < n ≤ 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: Postcondition: `q` is an integer representing the number of test cases where 1 ≤ `q` ≤ 100, `M` is a list containing the integer division of `w` by 1, and `w` is the square root of `q`. If the current value of `w` is equal to its integer division by 1 and is greater than or equal to `x` - 1, then `M` contains the integer division of `w` by 1.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: q is an integer between 1 and 100 inclusive, M is an empty list, w is the integer part of the square root of q, and x is not used or defined in the final state.
    return M
    #The program returns an empty list M
#Overall this is what the function does:The function accepts two parameters, `q` and `x`. `q` represents the number of test cases, where 1 ≤ q ≤ 100. For each test case, `x` is an integer such that 1 ≤ x < n ≤ 10^9. The function calculates the integer part of the square root of `q` and checks if it meets certain conditions. If these conditions are satisfied, it adds the integer part of the square root or its divisors to the list `M`. Finally, the function returns an empty list `M`.

