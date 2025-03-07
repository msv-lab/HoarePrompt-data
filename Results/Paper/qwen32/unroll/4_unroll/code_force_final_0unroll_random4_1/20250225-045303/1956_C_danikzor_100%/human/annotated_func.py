#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 500) representing the number of test cases. Each of the following t lines contains a single integer n (1 ≤ n ≤ 500), which represents the size of the n × n matrix a. The sum of n^2 over all test cases does not exceed 5 · 10^5.
def func_1():
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: n * (n + 1) * (4 * n - 1) // 6, 2 * n (where n is the size of the n × n matrix)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: For each test case with input `n`, the output consists of `2 * n` lines, each line starting with either `1` or `2`, followed by the current `i` value, and then the sequence of numbers from `n` down to `1`.
#Overall this is what the function does:The function `func_1` processes multiple test cases, where each test case consists of an integer `n` representing the size of an `n × n` matrix. For each test case, it prints a specific mathematical result and then prints `2 * n` lines, each starting with either `1` or `2`, followed by the current row number and a sequence of numbers from `n` down to `1`.

