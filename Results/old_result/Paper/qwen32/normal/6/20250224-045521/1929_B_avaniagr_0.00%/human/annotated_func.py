#State of the program right berfore the function call: The function receives input for multiple test cases. Each test case consists of two integers, n and k, where 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2. n represents the size of the square grid, and k represents the minimum number of diagonals that must contain at least one colored cell.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        print((k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k ==
            4 * n - 2))
        
    #State: The output state is the concatenation of the printed values for all test cases, with each value on a new line.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k`. It calculates and prints a value for each test case, which indicates the result of a condition related to coloring cells in an `n` by `n` grid such that at least `k` diagonals contain at least one colored cell.

