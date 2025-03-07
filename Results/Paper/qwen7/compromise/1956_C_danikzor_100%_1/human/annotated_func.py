#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n^2 over all test cases does not exceed 5 × 10^5.
def func_1():
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: (n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: Output State: The program prints two lines for each value of `i` from 1 to `n`. Each line starts with either 1 or 2, followed by the current value of `i`, and then the numbers from `n` down to 1. This process repeats `n` times.
#Overall this is what the function does:The function processes an integer `n` (1 ≤ n ≤ 500) and calculates and prints a mathematical expression `(n * (n + 1) * (4 * n - 1) // 6)` along with `2 * n`. It then prints two lines for each value of `i` from 1 to `n`, each starting with either 1 or 2, followed by the current value of `i`, and then the numbers from `n` down to 1. The function does not return any value but prints the results directly.

