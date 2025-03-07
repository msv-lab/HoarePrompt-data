#State of the program right berfore the function call: The function should take two parameters, n and k, where n is an integer representing the size of the square grid (2 ≤ n ≤ 10^8), and k is an integer representing the minimum number of diagonals that should have at least one colored cell (1 ≤ k ≤ 4n - 2).
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * (n + (n - 2)):
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: The loop will execute for each pair of inputs (n, k) provided. For each pair, if k is 1, the output will be 1. If k is between 2 and 2 * (n + (n - 2)), the output will be the ceiling of k divided by 2. If k is greater than 2 * (n + (n - 2)), the output will be k divided by 2, rounded down, plus 1. The loop will continue to execute until all input pairs have been processed.
#Overall this is what the function does:The function processes multiple pairs of integers (n, k) provided through user input, where `n` is the size of a square grid and `k` is the minimum number of diagonals that should have at least one colored cell. For each pair, it outputs the minimum number of cells that need to be colored to satisfy the condition. If `k` is 1, the output is 1. If `k` is between 2 and 2 * (n + (n - 2)), the output is the ceiling of `k` divided by 2. If `k` is greater than 2 * (n + (n - 2)), the output is `k` divided by 2, rounded down, plus 1. The function continues processing until all input pairs have been handled.

