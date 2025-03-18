#State of the program right berfore the function call: a and b are positive integers such that \(1 \leq a \leq n\) and \(1 \leq b \leq m\).
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: Output State: The greatest common divisor (GCD) of a and b.
    #
    #Explanation: The given loop implements the Euclidean algorithm for finding the greatest common divisor (GCD) of two numbers, `a` and `b`. After the loop finishes executing, the variable `a` will hold the GCD of the initial values of `a` and `b`.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of `a` and `b`
#Overall this is what the function does:The function accepts two positive integers `a` and `b` as input and returns their greatest common divisor (GCD). After execution, the variable `a` contains the GCD of the initial values of `a` and `b`.

#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6 and the sum of all m and n over all test cases does not exceed 2 ⋅ 10^6.
def func_2(n, m):
    cnt = 0
    for i in range(1, m):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + x // y + (i > 1)
        
    #State: Output State: `cnt` is the sum of `x // y + (i > 1)` for each `i` in the range from 1 to `m-1`. This value depends on the specific values of `n` and `m`, but generally, it represents the cumulative result of the division and conditional addition operations performed within the loop.
    if (cnt == 0) :
        return 1
        #The program returns 1
    #State: `cnt` is the sum of `x // y + (i > 1)` for each `i` in the range from 1 to `m-1`, and `cnt` is not equal to 0
    return cnt
    #The program returns a value of cnt which is the sum of x // y + (i > 1) for each i in the range from 1 to m-1, and cnt is not equal to 0.
#Overall this is what the function does:The function accepts two positive integers `n` and `m` (where 1 ≤ n, m ≤ 2⋅10^6). It calculates the sum of `x // y + (i > 1)` for each `i` in the range from 1 to `m-1`, where `x = n - (i * i - i)` and `y = i * i`. If this sum equals 0, the function returns 1; otherwise, it returns the calculated sum.

