#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. Each of the next t lines contains two integers n and k where 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: The loop has executed `t` times, printing `t` values based on the condition `4 * n - 2 == k`. Each value is either `k // 2 + 1` if the condition is true, or `ceil(k / 2)` if the condition is false.
#Overall this is what the function does:The function processes a series of test cases, each defined by two integers `n` and `k`. For each test case, it calculates and prints a specific integer value based on whether `k` equals `4 * n - 2`. If `k` equals `4 * n - 2`, it prints `k // 2 + 1`; otherwise, it prints the ceiling of `k / 2`.

