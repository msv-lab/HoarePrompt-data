#State of the program right berfore the function call: a and b are positive integers such that 1 <= a <= n and 1 <= b <= m.
def func_1(a, b):
    while b:
        a, b = b, a % b
        
    #State: Output State: The values of `a` and `b` will be such that `b` is 0 and `a` is the greatest common divisor (GCD) of the initial values of `a` and `b`.
    #
    #Explanation: The given loop implements the Euclidean algorithm for finding the greatest common divisor (GCD) of two numbers. After the loop completes all its iterations, `a` will hold the GCD of the initial values of `a` and `b`, and `b` will be 0 since the remainder becomes 0 when the GCD is found.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of `a` and `b`, with `b` being 0.
#Overall this is what the function does:The function accepts two positive integer parameters `a` and `b`. It computes their greatest common divisor (GCD) using the Euclidean algorithm. Upon completion, it returns the GCD of `a` and `b`, with `b` being set to 0.

#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6 and the sum of n and m over all test cases does not exceed 2 ⋅ 10^6.
def func_2(n, m):
    cnt = 0
    for i in range(1, m):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + x // y + (i > 1)
        
    #State: Output State: `cnt` is 1, `i` is 4, `m` must be greater than 3, `x` is -20, `y` is 16.
    #
    #Explanation: The loop continues until `i` reaches `m`. From the given information, we can see that after the third iteration, `i` is 3 and `m` must be greater than 3. Since `i` increments by 1 each iteration, the next value of `i` will be 4. However, the value of `cnt` does not change from the third iteration because the condition `i > 1` is still true but the term `x // y` results in a negative or zero value, which does not contribute to increasing `cnt`. Therefore, `cnt` remains at 1. The values of `x` and `y` continue to decrease as per the formula `x = n - (i * i - i)` and `y = i * i`, respectively. For `i = 4`, `x` becomes `-20` and `y` becomes `16`.
    if (cnt == 0) :
        return 1
        #The program returns 1
    #State: `cnt` is 1, `i` is 4, `m` must be greater than 3, `x` is -20, `y` is 16, `cnt` is not equal to 0
    return cnt
    #The program returns 1
#Overall this is what the function does:The function accepts two positive integers `n` and `m` (where 1 ≤ n, m ≤ 2⋅10^6). It iterates through a loop from 1 to `m-1`, calculating values for `x` and `y` based on the current index `i`. It updates a counter `cnt` based on these values. If `cnt` remains 0 after the loop, the function returns 1; otherwise, it also returns 1. The function always returns 1 regardless of the input values.

