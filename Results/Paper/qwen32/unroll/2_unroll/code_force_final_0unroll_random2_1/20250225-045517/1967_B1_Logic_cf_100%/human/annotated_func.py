#State of the program right berfore the function call: Each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 2 · 10^6. The function will be called multiple times with a total of t test cases, where 1 ≤ t ≤ 10^4. The sum of n and the sum of m across all test cases do not exceed 2 · 10^6.
def func():
    t = int(input())
    for T in range(t):
        [n, m] = input().split()
        
        [n, m] = [int(n), int(m)]
        
        ans = n
        
        for b in range(2, min(n, m) + 1):
            ans = ans + (n + b) // (b * b)
        
        print(ans)
        
    #State: The variable `ans` holds the final computed value for each test case, and it is printed after processing each test case. The variables `n`, `m`, and `b` are local to the loop and do not persist after the loop's execution for each test case. The variable `T` is the loop index for iterating through the test cases and does not persist after the loop completes. The input variable `t` remains unchanged as it represents the total number of test cases.
#Overall this is what the function does:The function reads multiple test cases, each consisting of two positive integers `n` and `m`, and for each test case, it computes and prints a value `ans` based on these integers. The value `ans` is calculated by starting with `n` and adding to it the integer division of `(n + b)` by `(b * b)` for each `b` from 2 to the minimum of `n` and `m`. The function handles up to `t` test cases, where `t` is provided as input.

