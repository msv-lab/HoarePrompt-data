#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, each test case consists of two integers n and k such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: Output State: The output state will consist of `t` lines, each containing either `1` or `n`. For each iteration `i` from `0` to `t-1`, the value printed depends on the condition `k >= n - 1`. If the condition is true, `1` is printed; otherwise, `n` is printed. The specific values of `n` and `k` for each iteration are provided by user input.
#Overall this is what the function does:The function processes up to 1000 test cases, where each test case consists of two integers \( n \) and \( k \). For each test case, it checks if \( k \) is greater than or equal to \( n - 1 \). If true, it prints 1; otherwise, it prints \( n \). The function outputs a line for each test case, resulting in a total of up to 1000 lines of output.

