#State of the program right berfore the function call: The function should take two parameters, n and k, where n is an integer representing the size of the square grid (2 ≤ n ≤ 10^8), and k is an integer representing the minimum number of diagonals that should have at least one colored cell (1 ≤ k ≤ 4n - 2).
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: The values of `n` and `k` are updated based on the input provided in each iteration of the loop, but `t` remains unchanged. The loop prints a value for each iteration, but does not modify `t`.
#Overall this is what the function does:The function reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `n` is the size of a square grid (2 ≤ n ≤ 10^8) and `k` is the minimum number of diagonals that should have at least one colored cell (1 ≤ k ≤ 4n - 2). It then prints the number of ways to color the grid such that at least `k` diagonals have at least one colored cell. The function does not return any value; it only prints the results for each test case. The values of `n` and `k` are updated for each iteration of the loop, but `t` remains unchanged throughout the function's execution.

