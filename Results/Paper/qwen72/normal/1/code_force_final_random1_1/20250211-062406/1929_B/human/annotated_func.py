#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 1000, representing the number of test cases. For each test case, n and k are integers where 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2, representing the size of the square grid and the minimum number of diagonals that must contain at least one colored cell, respectively.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: `t` is 0, all `n` and `k` values provided by the user have been processed. For each pair of `n` and `k`, if \(4 \times n - 2 = k\), the output was \(k // 2 + 1\). Otherwise, the output was `ceil(k / 2)`.
#Overall this is what the function does:The function processes a series of test cases, where each test case involves a square grid of size `n` and a requirement to color at least `k` diagonals. For each test case, it calculates and prints the minimum number of cells that need to be colored to meet the requirement. If `k` equals `4 * n - 2`, it prints `k // 2 + 1`; otherwise, it prints `ceil(k / 2)`. After processing all test cases, the function completes without returning any value.

