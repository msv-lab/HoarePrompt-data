#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 676, and for each test case, n and k are integers such that 1 ≤ n ≤ 26 and 1 ≤ k ≤ 26.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        print('abcdefghijklmnopqrstuvwxyz'[:k] * n)
        
    #State: Output State: The loop will execute `t` times. After all iterations, the variable `i` will have the value of `t-1`, `n` will be the integer from the last input provided during the loop's execution, and `k` will be the second integer from the last input provided during the loop's execution. The value of `t` will remain as it was initially provided and must be within the range 1 ≤ t ≤ 676.
    #
    #This means that if the loop runs `t` times, the final state of the loop will show that `i` has reached `t-1`, and the values of `n` and `k` will be those of the last input pair processed by the loop.
#Overall this is what the function does:The function processes up to 676 test cases. For each test case, it reads two integers \( n \) and \( k \) where \( 1 \leq n \leq 26 \) and \( 1 \leq k \leq 26 \). It then prints a string consisting of the first \( k \) characters of the alphabet, repeated \( n \) times. After processing all test cases, the function does not return any value but outputs the specified strings for each test case.

