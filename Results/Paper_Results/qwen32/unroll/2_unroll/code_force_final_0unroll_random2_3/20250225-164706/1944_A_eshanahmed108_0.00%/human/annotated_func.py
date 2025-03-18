#State of the program right berfore the function call: Each test case contains two integers n and k where 1 ≤ n ≤ 100 and 0 ≤ k ≤ \frac{n \cdot (n - 1)}{2}. There are t test cases where 1 ≤ t ≤ 10^3.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        print(n if n - k <= 1 else 1)
        
    #State: a series of numbers where each number is either `n` or `1` depending on the condition `n - k <= 1` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k`. For each test case, it prints `n` if `n - k` is less than or equal to 1, otherwise it prints `1`.

