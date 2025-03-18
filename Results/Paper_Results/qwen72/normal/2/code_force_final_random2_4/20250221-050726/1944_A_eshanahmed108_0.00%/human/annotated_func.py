#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^3, representing the number of test cases. Each test case consists of two integers n and k, where 1 ≤ n ≤ 100 and 0 ≤ k ≤ n * (n - 1) / 2, representing the number of islands and the maximum number of bridges that can be destroyed, respectively.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: _ is a placeholder, `t` is an integer where 1 ≤ t ≤ 10^3, `n` and `k` are integers read from the input.
#Overall this is what the function does:The function reads multiple test cases from the standard input. Each test case consists of two integers, `n` and `k`, representing the number of islands and the maximum number of bridges that can be destroyed, respectively. For each test case, the function prints the number of islands (`n`) if the difference between the number of islands and the number of bridges that can be destroyed (`n - k`) is less than or equal to 1; otherwise, it prints 1. After processing all test cases, the function completes, and the state of the program includes the number of test cases processed (`t`), the last values of `n` and `k` read from the input, and the placeholder `_` used in the loop.

