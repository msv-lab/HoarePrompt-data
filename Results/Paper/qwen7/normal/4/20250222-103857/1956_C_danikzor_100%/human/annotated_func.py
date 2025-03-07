#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n² over all test cases does not exceed 5 × 10⁵.
def func_1():
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: (n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: Output State: The loop will execute `n` times, with `i` ranging from 1 to `n`. For each iteration, `i` will take on the value of the current iteration number, and `n` must be at least 3 for the loop to complete all its iterations.
    #
    #In more detail, after the loop completes all its iterations, `i` will be equal to `n`, and `n` can be any integer from 3 up to 500 (as per the initial constraints).
#Overall this is what the function does:The function processes an integer `n` (1 ≤ n ≤ 500) and calculates two values: `(n * (n + 1) * (4 * n - 1) // 6)` and `2 * n`. It then prints these values followed by executing a loop that prints two sets of output for each value of `i` from 1 to `n`. After completing all iterations, the function concludes with `i` equal to `n` and `n` within the range of 3 to 500.

