#State of the program right berfore the function call: a and b are positive integers such that \(1 \leq a \leq n\) and \(1 \leq b \leq m\).
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: Output State: The values of `a` and `b` will be such that `b` is 0 and `a` is the greatest common divisor (GCD) of the initial values of `a` and `b`.
    #
    #Explanation: The given loop implements the Euclidean algorithm to find the greatest common divisor (GCD) of two numbers `a` and `b`. After the loop completes all its iterations, `a` will hold the GCD of the initial values of `a` and `b`, and `b` will be 0 because the algorithm continues until `b` becomes 0.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of `a` and `b`, with `b` being 0.
#Overall this is what the function does:The function accepts two positive integer parameters `a` and `b`. It computes their greatest common divisor (GCD) using the Euclidean algorithm, updating the values of `a` and `b` within the process. Upon completion, the function returns the GCD of the initial values of `a` and `b`, with `b` being 0.

#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^6 and the sum of all m and n over all test cases does not exceed 2⋅10^6.
def func_2(n, m):
    cnt = 0
    for i in range(1, m):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + x // y + (i > 1)
        
    #State: Output State: `m` must be greater than 1; `i` is equal to `m`; `x` is `n - (m * m - m)`, `y` is `m * m`; `cnt` is the sum of `x // y + (m > 1)` added for each iteration from `i` starting from 1 up to `m-1`.
    #
    #In simpler terms, after the loop has executed all its iterations, `m` will be the final value it was set to, `i` will be equal to `m`, `x` will be calculated as `n - (m * m - m)`, `y` will be `m * m`, and `cnt` will be the cumulative sum of `x // y + 1` for each `i` from 1 to `m-1`.
    if (cnt == 0) :
        return 1
        #The program returns 1
    #State: `m` is greater than 1, `i` is equal to `m`, `x` is `n - (m * m - m)`, `y` is `m * m`, and `cnt` is the sum of `x // y + 1` for each `i` from 1 to `m-1`
    return cnt
    #The program returns the sum of x // y + 1 for each i from 1 to m-1, where x is n - (m * m - m), y is m * m, and n is equal to m.
#Overall this is what the function does:The function accepts two parameters, `n` and `m`, both positive integers with 1 ≤ n, m ≤ 2⋅10^6. It calculates the sum of `x // y + 1` for each `i` from 1 to `m-1`, where `x` is `n - (m * m - m)` and `y` is `m * m`. If this sum equals 0, the function returns 1; otherwise, it returns the calculated sum.

