#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n and k are integers where 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2, representing the size of the square grid and the minimum number of diagonals that must contain at least one colored cell, respectively.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: `t` is an input integer where 1 ≤ t ≤ 1000, `_` has iterated through the range from 0 to `t-1`, `n` and `k` are integers read from input for each iteration. For each iteration, if \(4 \times n - 2\) equals `k`, the output is `k // 2 + 1`. Otherwise, the output is `ceil(k / 2)`.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads two integers `n` and `k`, where `n` is the size of a square grid and `k` is the minimum number of diagonals that must contain at least one colored cell. The function then prints either `k // 2 + 1` if `4 * n - 2` equals `k`, or `ceil(k / 2)` otherwise. After processing all test cases, the function completes without returning any value.

