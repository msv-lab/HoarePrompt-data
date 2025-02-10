#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 \cdot 10^6, and the sum of all n and the sum of all m over all test cases do not exceed 2 \cdot 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = 0
        
        for b in range(1, min(n, m) + 1):
            ans = ans + n // b + 1
        
        print(ans)
        
    #State: The final value of `ans` will be the sum of `n // b + 1` for each `b` in the range from 1 to the minimum of `n` and `m` for all iterations of `T` from 0 to `t-1`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two positive integers \( n \) and \( m \). For each test case, it calculates the sum of \( n // b + 1 \) for each \( b \) in the range from 1 to the minimum of \( n \) and \( m \). After processing all test cases, it prints the result for each test case.

