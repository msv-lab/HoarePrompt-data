#State of the program right berfore the function call: The input consists of multiple test cases. Each test case is defined by two integers n and k, where n (1 ≤ n ≤ 100) represents the number of islands and k (0 ≤ k ≤ n * (n - 1) / 2) represents the maximum number of bridges Dominater can destroy.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: a series of integers where each integer is the result of the condition `n - k <= 1` for each test case, printed one per line.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` (number of islands) and `k` (maximum number of bridges that can be destroyed). For each test case, it prints the maximum number of islands that can remain connected after destroying at most `k` bridges. If `n - k` is less than or equal to 1, it prints `n`; otherwise, it prints 1.

