#State of the program right berfore the function call: Each test case consists of two integers n and k, where 1 ≤ n ≤ 100 and 0 ≤ k ≤ n * (n - 1) / 2. There are t test cases, where 1 ≤ t ≤ 10^3.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: the sequence of printed values for each test case, determined by the condition `n if n - k <= 1 else 1`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k`. For each test case, it prints `n` if `n - k` is less than or equal to 1; otherwise, it prints 1.

