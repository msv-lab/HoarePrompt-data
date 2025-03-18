#State of the program right berfore the function call: Each test case contains a single integer n (1 ≤ n ≤ 500) representing the size of the n×n matrix filled with zeroes. The number of test cases t is between 1 and 500, and the sum of n^2 over all test cases does not exceed 5 × 10^5.
def func_1():
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: n * (n + 1) * (4 * n - 1) // 6, 2 * n (where n is the size of the n×n matrix)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: The output will consist of `2 * n` lines, where each pair of lines corresponds to an iteration of `i` from 1 to `n`. The first line of each pair is `1, i, n, n-1, ..., 1` and the second line is `2, i, n, n-1, ..., 1`.
#Overall this is what the function does:The function reads an integer `n` from the input, prints a specific mathematical result based on `n`, and then prints `2 * n` lines, each pair of lines corresponding to an iteration of `i` from 1 to `n`. The first line of each pair contains `1, i, n, n-1, ..., 1`, and the second line contains `2, i, n, n-1, ..., 1`.

