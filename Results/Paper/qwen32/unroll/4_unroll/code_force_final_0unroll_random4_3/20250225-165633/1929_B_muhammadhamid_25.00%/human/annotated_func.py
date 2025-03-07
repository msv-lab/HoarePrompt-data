#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 1000) — the number of test cases. Each of the following t lines contains two integers n and k (2 ≤ n ≤ 10^8, 1 ≤ k ≤ 4n - 2) — the size of the square grid and the minimum number of diagonals in which there should be at least one colored cell.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * n:
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: The output state consists of t lines, each containing the minimum number of rows that need to be colored to ensure that at least k diagonals have at least one colored cell in an n x n grid. For each test case, if k is 1, the output is 1. If k is less than or equal to 2 * n, the output is the ceiling of k divided by 2. Otherwise, the output is k divided by 2 plus one.
#Overall this is what the function does:The function processes multiple test cases, each defined by the size of a square grid `n` and a minimum number of diagonals `k` that should contain at least one colored cell. For each test case, it calculates and outputs the minimum number of rows that need to be colored to meet the requirement on diagonals.

