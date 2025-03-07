#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 ⋅ 10^6. It is also guaranteed that the sum of n and the sum of m over all test cases do not exceed 2 ⋅ 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each T in range(t), there is a corresponding ans calculated based on the given formula, and these ans values are printed for each iteration.
#Overall this is what the function does:The function processes a series of test cases, each containing two positive integers \( n \) and \( m \). For each test case, it calculates a value \( ans \) using a specific formula involving \( n \) and \( b \) (where \( b \) ranges from 2 to the minimum of \( n \) and \( m \)). The function then prints the calculated \( ans \) for each test case. The function does not return any value but prints the results for each test case.

