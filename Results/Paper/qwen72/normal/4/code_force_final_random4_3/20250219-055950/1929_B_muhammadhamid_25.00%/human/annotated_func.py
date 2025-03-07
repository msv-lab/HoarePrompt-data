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
        
    #State: The loop has executed `int(input())` times, and for each iteration `_` incremented from 0 to `int(input()) - 1`. For each pair of input integers `n` and `k`, if `k` was 1, the program printed 1 and moved to the next iteration. If `k` was less than or equal to `2 * n`, the program printed the ceiling of `k / 2`. If `k` was greater than `2 * n`, the program printed `k // 2 + 1`. The values of `n` and `k` for each iteration were provided by user input and are not retained between iterations.
#Overall this is what the function does:The function processes multiple pairs of integers `n` and `k` provided by the user, where `n` is the size of a square grid and `k` is the minimum number of diagonals that should have at least one colored cell. For each pair, the function prints a number based on the following rules: if `k` is 1, it prints 1; if `k` is less than or equal to `2 * n`, it prints the ceiling of `k / 2`; if `k` is greater than `2 * n`, it prints `k // 2 + 1`. The function does not return any value; it only prints the results to the console. After processing all pairs, the function concludes.

