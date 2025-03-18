#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, each test case consists of two integers n and k such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: Output State: The output state will consist of a series of lines, each containing either '1' or 'n - 1', where 'n' and 'k' are integers entered by the user for each iteration of the loop. The number of lines will be equal to the value of `t`. For each line, if `k` is greater than or equal to `n - 1`, the line will contain '1'; otherwise, it will contain 'n - 1'.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( n \) and \( k \). For each test case, it checks whether \( k \) is greater than or equal to \( n - 1 \). If true, it prints '1'; otherwise, it prints \( n - 1 \). The function reads these values from user input and outputs the results, repeating this process for \( t \) times, where \( t \) is also provided by the user and represents the number of test cases.

