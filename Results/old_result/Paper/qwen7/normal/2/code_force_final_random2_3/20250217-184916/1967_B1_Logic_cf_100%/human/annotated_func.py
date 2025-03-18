#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6, and the sum of n or m over all test cases does not exceed 2 ⋅ 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: After the loop executes all iterations, `t` remains greater than 0, `b` is set to `min(n, m) + 1`, `ans` is the cumulative sum of `(n + b) // (b * b)` for each `b` from 2 to `min(n, m)` inclusive, and `[n, m]` contains the integer values of the split input strings.
#Overall this is what the function does:The function processes a series of test cases, each containing two positive integers \( n \) and \( m \). It calculates the value of \( ans \) by initializing it to \( n \) and then adding to it the result of \( (n + b) // (b * b) \) for each integer \( b \) from 2 up to the minimum of \( n \) and \( m \). After processing all test cases, it prints the final value of \( ans \) for each case.

