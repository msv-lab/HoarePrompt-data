#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, each test case consists of two integers n and k such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: t is a positive integer between 1 and 1000 inclusive, i is 3, n is the first integer from the input, k is the second integer from the first iteration's input. The values of t, i, n, and k remain unchanged regardless of whether the condition k >= n - 1 is true or false for each iteration.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( n \) and \( k \). For each test case, it checks if \( k \) is greater than or equal to \( n - 1 \). If true, it prints 1; otherwise, it prints \( n - 1 \). The function reads these test cases from standard input and does not return any value.

