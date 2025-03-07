#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. Each of the following t lines contains two integers n and k (2 ≤ n ≤ 10^8, 1 ≤ k ≤ 4n - 2) — the size of the square grid and the minimum number of diagonals that should contain at least one colored cell.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        print((k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k ==
            4 * n - 2))
        
    #State: the concatenation of the results of each test case, each printed on a new line.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k`. For each test case, it calculates and prints a result based on the conditions involving the size of a square grid `n` and the minimum number of diagonals `k` that should contain at least one colored cell.

