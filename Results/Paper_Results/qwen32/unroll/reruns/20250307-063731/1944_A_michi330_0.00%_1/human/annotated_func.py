#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10³), the number of test cases. Each test case consists of a single line containing two integers n and k (1 ≤ n ≤ 100, 0 ≤ k ≤ n * (n - 1) / 2).
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n - 1)
        
    #State: the values of `n` and `k` for each test case have been processed, and for each test case, `1` is printed if `k` is greater than or equal to `n - 1`, otherwise `n - 1` is printed. The variable `i` will be equal to `t` after the loop completes, and `t` remains unchanged.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of two integers `n` and `k`. For each test case, it prints `1` if `k` is greater than or equal to `n - 1`; otherwise, it prints `n - 1`.

