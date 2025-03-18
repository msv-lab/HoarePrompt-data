#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n and k are integers such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: Output State: The output state will consist of a series of numbers printed based on the condition `n if n - k <= 1 else 1` for each test case. For each test case, if the value of `n - k` is less than or equal to 1, the number `n` will be printed; otherwise, the number `1` will be printed. The total number of outputs will be equal to the number of test cases provided as input.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \). For each test case, it prints \( n \) if \( n - k \leq 1 \), otherwise it prints \( 1 \). The function does not return any value but prints the results for each test case.

