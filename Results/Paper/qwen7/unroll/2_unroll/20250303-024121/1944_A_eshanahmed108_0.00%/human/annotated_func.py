#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, each test case consists of two integers n and k such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ (n * (n - 1)) / 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: Output State: The output state will consist of a series of numbers printed based on the condition `n if n - k <= 1 else 1` for each test case. For each test case, if `n - k` is less than or equal to 1, the output will be `n`, otherwise, it will be `1`. The number of outputs will be equal to the number of test cases provided by the input.
#Overall this is what the function does:The function processes up to 1000 test cases, where for each test case, it reads two integers \( n \) and \( k \). Based on the condition \( n - k \leq 1 \), it prints either \( n \) or 1. The final state of the program is a series of outputs, each corresponding to the result of the condition check for each test case.

