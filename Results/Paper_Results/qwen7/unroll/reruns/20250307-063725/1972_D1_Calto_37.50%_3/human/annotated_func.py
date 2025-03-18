#State of the program right berfore the function call: a and b are positive integers such that \(1 \leq a \leq n\) and \(1 \leq b \leq m\).
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: Output State: The output state is that `a` contains the greatest common divisor (GCD) of the initial values of `a` and `b`, and `b` is 0.
    #
    #The loop implements the Euclidean algorithm to find the GCD of two numbers. Initially, `a` and `b` are positive integers within specified ranges. After the loop completes, `a` will hold the GCD of the original `a` and `b`, and `b` will be 0 because the Euclidean algorithm continues to replace `b` with the remainder of `a` divided by `b` until `b` becomes 0.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of `a` and `b`, with `b` being 0.
#Overall this is what the function does:The function accepts two positive integer parameters `a` and `b`. It calculates the greatest common divisor (GCD) of `a` and `b` using the Euclidean algorithm. After the calculation, the function returns the GCD of the initial values of `a` and `b`, with `b` being set to 0.

#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6 and the sum of all m and n over all test cases does not exceed 2 ⋅ 10^6.
def func_2(n, m):
    cnt = 0
    for i in range(1, m):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + x // y + (i > 1)
        
    #State: Output State: `cnt` is the sum of the series where for each `i` from 1 to `m-1`, we compute `x = n - (i * i - i)` and `y = i * i`, then add `x // y + (i > 1)` to `cnt`.
    if (cnt == 0) :
        return 1
        #The program returns 1
    #State: `cnt` is the sum of the series where for each `i` from 1 to `m-1`, we compute `x = n - (i * i - i)` and `y = i * i`, then add `x // y + (i > 1)` to `cnt`. The value of `cnt` is not zero.
    return cnt
    #The program returns the sum of the series where for each i from 1 to m-1, we compute x = n - (i * i - i) and y = i * i, then add x // y + (i > 1) to cnt. The value of cnt is not zero.
#Overall this is what the function does:The function accepts two positive integers \( n \) and \( m \), both constrained to be between 1 and \( 2 \times 10^6 \). If the computed sum \( cnt \) is zero, the function returns 1. Otherwise, it returns the non-zero sum \( cnt \) which is the result of a series calculation involving \( n \) and \( m \).

