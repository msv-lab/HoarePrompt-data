#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n and k are integers satisfying 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: Output State: The output state will consist of `t` lines, where each line contains either `1` or `n` based on the condition `k >= n - 1` for each pair of inputs `(n, k)`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( n \) and \( k \). For each test case, it checks if \( k \) is greater than or equal to \( n - 1 \). If true, it prints 1; otherwise, it prints \( n \). The function outputs \( t \) lines, where \( t \) is the number of test cases, and each line contains either 1 or \( n \) based on the condition.

