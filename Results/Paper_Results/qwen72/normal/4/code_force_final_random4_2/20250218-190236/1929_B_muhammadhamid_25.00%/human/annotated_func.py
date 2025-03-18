#State of the program right berfore the function call: The function should take two parameters, n and k, where n is an integer representing the size of the square grid (2 ≤ n ≤ 10^8), and k is an integer representing the minimum number of diagonals that should have at least one colored cell (1 ≤ k ≤ 4n - 2).
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
        
    #State: The loop has executed all iterations, and for each iteration, `n` and `k` were assigned new values from the input. If `k` was 1, the iteration was skipped, and the values of `n` and `k` remained unchanged. If `k` was less than or equal to 2 * n, the condition `k <= 2 * n` was true, and the result of `math.ceil(k / 2)` was printed. If `k` was greater than 2 * n, the condition `k > 2 * n` was true, and the result of `k // 2 + 1` was printed. The values of `n` and `k` for each iteration are independent and do not affect subsequent iterations.
#Overall this is what the function does:The function reads multiple pairs of integers `n` and `k` from the input, where `n` represents the size of a square grid and `k` represents the minimum number of diagonals that should have at least one colored cell. For each pair, the function prints the minimum number of cells that need to be colored to ensure that at least `k` diagonals have at least one colored cell. If `k` is 1, it prints 1. If `k` is less than or equal to 2 * n, it prints the ceiling of `k / 2`. If `k` is greater than 2 * n, it prints `k // 2 + 1`. The function does not return any value, and each iteration is independent of the others.

