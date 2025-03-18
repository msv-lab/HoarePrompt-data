#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n and k are integers where 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2, representing the size of the square grid and the minimum number of diagonals that must contain at least one colored cell, respectively.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if k % 2 == 0 and k // 2 % 2 == 1:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: `t` is an input integer where 1 ≤ t ≤ 1000, `_` is `t-1`, `n` is the first integer from the last input, `k` is the second integer from the last input. If `k` is even and half of `k` is odd, the program prints `k // 2 + 1`. Otherwise, the program prints `ceil(k / 2)`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `k`, representing the size of a square grid and the minimum number of diagonals that must contain at least one colored cell, respectively. The function then calculates and prints a value for each test case: if `k` is even and half of `k` is odd, it prints `k // 2 + 1`; otherwise, it prints `ceil(k / 2)`. After processing all test cases, the function completes without returning any value.

