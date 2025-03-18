#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. Each of the following t lines contains two integers n and k (2 ≤ n ≤ 10^8, 1 ≤ k ≤ 4n - 2) — the size of the square grid and the minimum number of diagonals in which there should be at least one colored cell.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        if k <= 4 * n - 4:
            print(math.ceil(k / 2))
        elif k == 4 * n - 3:
            print(2 * n - 1)
        elif k == 4 * n - 2:
            print(2 * n)
        
    #State: the sequence of results printed for each test case, one per line.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` representing the size of a square grid and an integer `k` representing the minimum number of diagonals that should contain at least one colored cell. For each test case, it calculates and prints the minimum number of cells that need to be colored to satisfy the condition on `k` diagonals.

