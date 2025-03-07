#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 500) representing the number of test cases. Each test case consists of a single integer n (1 ≤ n ≤ 500) representing the size of the n x n matrix. The sum of n^2 over all test cases does not exceed 5 * 10^5.
def func_1():
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: n * (n + 1) * (4 * n - 1) // 6, 2 * n (where n is the size of the n x n matrix for each test case)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: For each test case with integer `n`, the output consists of `2 * n` lines. Each pair of lines for `i` from 1 to `n` is `1 i n n-1 ... 2 1` followed by `2 i n n-1 ... 2 1`.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the size of an `n x n` matrix. For each test case, it prints a specific sequence of numbers: first, it prints the value of the formula `n * (n + 1) * (4 * n - 1) // 6` followed by `2 * n`. Then, for each `i` from 1 to `n`, it prints two lines: the first line starts with `1 i` followed by numbers from `n` to `1`, and the second line starts with `2 i` followed by the same sequence of numbers from `n` to `1`.

