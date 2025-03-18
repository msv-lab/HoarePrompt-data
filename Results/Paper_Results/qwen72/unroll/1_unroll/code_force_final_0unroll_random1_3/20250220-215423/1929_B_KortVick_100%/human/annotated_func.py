#State of the program right berfore the function call: The function `func` is incomplete and does not match the problem description. The correct function definition should be `def min_cells_to_color(n, k):` where `n` is an integer representing the size of the square grid (2 ≤ n ≤ 10^8), and `k` is an integer representing the minimum number of diagonals that should have at least one colored cell (1 ≤ k ≤ 4n - 2).
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        
        if 4 * n - 2 == k:
            print(k // 2 + 1)
        else:
            print(ceil(k / 2))
        
    #State: The function `func` remains incomplete and does not match the problem description. The loop iterates `t` times, each time reading two integers `n` and `k` from the input, and prints the result of the condition check. After the loop, the values of `n` and `k` are the last values read from the input, and `t` is unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases. For each test case, it reads two integers `n` and `k` from the input, where `n` is the size of a square grid (2 ≤ n ≤ 10^8) and `k` is the minimum number of diagonals (1 ≤ k ≤ 4n - 2) that should have at least one colored cell. It then calculates and prints the minimum number of cells that need to be colored to meet the requirement. After processing all test cases, the function does not return any value, and the final state of the program includes the last values of `n` and `k` read from the input, and `t` remains unchanged.

