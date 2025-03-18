#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= n and 1 <= b <= m.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: Output State: The values of `a` and `b` will be the greatest common divisor (GCD) of the initial values of `a` and `b`.
    #
    #Explanation: The given loop implements the Euclidean algorithm for finding the greatest common divisor (GCD) of two numbers. In each iteration, `a` is replaced with `b`, and `b` is replaced with the remainder of `a` divided by `b` (`a % b`). This process continues until `b` becomes zero, at which point `a` holds the GCD of the original values of `a` and `b`.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of `a` and `b`
#Overall this is what the function does:The function accepts two positive integer parameters `a` and `b`. It calculates and returns their greatest common divisor (GCD) using the Euclidean algorithm. After execution, `a` contains the GCD of the initial values of `a` and `b`.

#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6 and the sum of n and the sum of m over all test cases does not exceed 2 ⋅ 10^6.
def func_2(n, m):
    cnt = 0
    for i in range(1, m):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + x // y + (i > 1)
        
    #State: Output State: `cnt` is the sum of the series where for each `i` from 1 to `m-1`, we calculate `x = n - (i * i - i)` and `y = i * i`, then add `x // y + (i > 1)` to `cnt`.
    if (cnt == 0) :
        return 1
        #The program returns 1
    #State: `cnt` is the sum of the series where for each `i` from 1 to `m-1`, we calculate `x = n - (i * i - i)` and `y = i * i`, then add `x // y + (i > 1)` to `cnt`. Additionally, `cnt` is not equal to 0
    return cnt
    #The program returns the sum of the series where for each i from 1 to m-1, we calculate x = n - (i * i - i) and y = i * i, then add x // y + (i > 1) to cnt, given that cnt is not equal to 0.
#Overall this is what the function does:The function accepts two positive integers `n` and `m` as parameters. It calculates a series sum based on the formula \( x = n - (i^2 - i) \) and \( y = i^2 \), adding \( x // y + (i > 1) \) to a counter `cnt` for each `i` from 1 to `m-1`. If the counter `cnt` equals 0, the function returns 1; otherwise, it returns the calculated sum.

