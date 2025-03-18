#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2 · 10^6. The sum of all n and the sum of all m across all test cases do not exceed 2 · 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: The program prints `t` lines, each containing the value of `ans` computed for the respective pair of `n` and `m` provided in the input.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `m`, computes a specific value `ans` based on these inputs, and prints `ans` for each test case.

