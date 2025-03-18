#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. For each test case, n and k are integers such that 1 ≤ n ≤ 100 and 0 ≤ k ≤ \frac{n \cdot (n - 1)}{2}.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: The loop has executed `t` times, with `i` ranging from 0 to `t-1`. For each iteration, `n` and `k` are read from the input. If `k` is greater than or equal to `n - 1`, the program prints `1`; otherwise, it prints `n`. The value of `t` remains unchanged and is still within the range 1 ≤ `t` ≤ 10^3.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `k`. For each test case, it prints `1` if `k` is greater than or equal to `n - 1`; otherwise, it prints `n`.

