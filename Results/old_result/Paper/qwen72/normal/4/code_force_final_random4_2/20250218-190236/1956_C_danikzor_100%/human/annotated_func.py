#State of the program right berfore the function call: The function `func_1` is expected to handle input and output for multiple test cases. Each test case contains a single integer n (1 ≤ n ≤ 500) representing the size of the n×n matrix. The function should ensure that the number of operations used does not exceed 2n for each test case.
def func_1():
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: n * (n + 1) * (4 * n - 1) // 6, 2 * n (where n is the input integer between 1 and 500)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: `n` must be greater than or equal to `n`, `i` is `n`
#Overall this is what the function does:The function `func_1` accepts an integer `n` (1 ≤ n ≤ 500) representing the size of an n×n matrix. It prints two values: the first is the result of the formula `n * (n + 1) * (4 * n - 1) // 6`, and the second is `2 * n`. For each integer `i` from 1 to `n`, it prints two lines: the first line starts with `1`, followed by `i`, and then the integers from `n` down to `1` in reverse order. The second line starts with `2`, followed by `i`, and then the same sequence of integers from `n` down to `1` in reverse order. After the function concludes, `n` remains unchanged, and `i` is equal to `n`.

