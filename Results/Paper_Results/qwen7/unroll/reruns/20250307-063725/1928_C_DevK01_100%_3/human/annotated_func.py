#State of the program right berfore the function call: q is an integer representing the number of test cases, and for each test case, x and n are integers such that 1 ≤ x < n ≤ 10^9.
def func_1(q, x):
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: `q` is an integer representing the number of test cases, `w` is the square root of `q`, and `M` is a list containing `w`. If `w` is an integer and greater than or equal to `x - 1`, then `M` contains `w`. Otherwise, `M` remains an empty list.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: M is an empty list.
    return M
    #The program returns an empty list M
#Overall this is what the function does:The function accepts two parameters, `q` and `x`. It calculates the square root of `q` and checks if it is an integer greater than or equal to `x - 1`. If so, it adds this value to the list `M`. Then, it iterates through all integers from 1 to the square root of `q`, checking if they are divisors of `q` and if they or their corresponding divisors (i.e., `q // i`) are greater than or equal to `x - 1`. If these conditions are met, the respective values are added to the list `M`. Finally, the function returns an empty list `M`.

