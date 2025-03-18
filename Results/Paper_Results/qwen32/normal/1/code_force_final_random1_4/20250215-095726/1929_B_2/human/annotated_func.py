#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. For each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: The loop has executed `t` times, and the final values are `t` (unchanged), `n` and `k` from the last iteration, and `_` equal to `t`.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `k`. For each test case, it calculates and prints a specific value based on the relationship between `n` and `k`. If `k` equals `4n - 2`, it prints `k // 2 + 1`; otherwise, it prints the ceiling of `k / 2`.

