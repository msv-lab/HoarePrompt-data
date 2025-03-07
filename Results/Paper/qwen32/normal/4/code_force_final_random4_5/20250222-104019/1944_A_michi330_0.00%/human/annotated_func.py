#State of the program right berfore the function call: The function receives multiple test cases. Each test case is a tuple of two integers (n, k) where n (1 ≤ n ≤ 100) represents the number of islands and k (0 ≤ k ≤ n * (n - 1) / 2) represents the maximum number of bridges Dominater can destroy.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: The loop has processed all `t` test cases. For each test case, the program has printed either `1` if `k` is greater than or equal to `n - 1`, or `n - 1` if `k` is less than `n - 1`. The variable `i` has reached the value of `t`, indicating that all iterations are completed.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of two integers, `n` (number of islands) and `k` (maximum number of bridges that can be destroyed). For each test case, it prints `1` if `k` is greater than or equal to `n - 1`, otherwise it prints `n - 1`.

