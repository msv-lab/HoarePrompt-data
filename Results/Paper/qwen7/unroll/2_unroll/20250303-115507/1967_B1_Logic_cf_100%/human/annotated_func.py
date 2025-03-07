#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 \cdot 10^6, and the sum of n and the sum of m over all test cases does not exceed 2 \cdot 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: Output State: t is an integer between 1 and 10^4 inclusive, and for each T in the range of t, there exists a corresponding ans which is calculated based on the given formula, and these ans values are printed individually for each T.
#Overall this is what the function does:The function processes a series of test cases, each containing two positive integers `n` and `m`. It calculates a value `ans` for each test case using a specific formula and prints the result. The function ensures that the total number of test cases `t` is within the range of 1 to 10^4, and for each test case, `n` and `m` are within the range of 1 to 2 * 10^6, with the sum of `n` and `m` across all test cases not exceeding 2 * 10^6. After processing all test cases, it prints the calculated `ans` for each test case.

