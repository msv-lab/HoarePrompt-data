#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, each test case consists of two integers n and k such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: The loop has executed all its iterations, with `t` being the initial input integer (an integer within the range 1 to 1000), `i` being `t + 1`, `n` being the first input integer from the first iteration, and `k` being the first input integer from the first iteration. No further changes have been made to `n` and `k` throughout the loop's execution.
#Overall this is what the function does:The function processes up to 1000 test cases, each consisting of two integers \( n \) and \( k \). For each test case, it checks if \( k \) is greater than or equal to \( n - 1 \). If true, it prints 1; otherwise, it prints \( n - 1 \). The function does not return any value but prints the result for each test case.

