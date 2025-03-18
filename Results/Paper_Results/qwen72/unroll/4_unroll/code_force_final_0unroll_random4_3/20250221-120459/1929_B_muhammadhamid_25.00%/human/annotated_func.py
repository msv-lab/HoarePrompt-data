#State of the program right berfore the function call: The function `func` is incomplete and does not match the problem description. The correct function definition should be `def min_cells_to_color(n, k):` where `n` is an integer such that 2 ≤ n ≤ 10^8, and `k` is an integer such that 1 ≤ k ≤ 4n - 2.
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
        
    #State: The loop has finished executing all iterations, and the function `func` remains incomplete and does not match the problem description. The values of `n` and `k` are not retained after each iteration, and the loop prints the minimum number of cells to color for each input pair `(n, k)`.
#Overall this is what the function does:The function reads multiple pairs of integers `n` and `k` from user input, where each pair is on a new line. For each pair, it calculates and prints the minimum number of cells that need to be colored based on the value of `k`. If `k` is 1, it prints 1. If `k` is less than or equal to `2 * n`, it prints the ceiling of `k / 2`. Otherwise, it prints `k // 2 + 1`. The function does not return any value; it only prints the results for each input pair. After processing all input pairs, the function concludes without retaining any state.

