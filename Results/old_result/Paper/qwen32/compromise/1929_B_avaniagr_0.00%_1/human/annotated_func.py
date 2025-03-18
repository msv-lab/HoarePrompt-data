#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. Each of the following t lines contains two integers n and k (2 ≤ n ≤ 10^8, 1 ≤ k ≤ 4n - 2) — the size of the square grid and the minimum number of diagonals that should contain at least one colored cell.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        print((k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k ==
            4 * n - 2))
        
    #State: a series of integers, each representing the result of one test case based on the provided logic.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers `n` and `k`. It calculates and outputs a result for each test case, which indicates whether it is possible to color a square grid of size `n` such that at least `k` diagonals contain at least one colored cell.

