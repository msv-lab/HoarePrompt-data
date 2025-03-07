#State of the program right berfore the function call: Each test case contains an integer n (1 ≤ n ≤ 500) representing the size of the n × n matrix filled with zeroes. The function should handle multiple test cases, with the total number of test cases t (1 ≤ t ≤ 500) and the sum of n^2 over all test cases not exceeding 5 × 10^5.
def func_1():
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: n * (n + 1) * (4 * n - 1) // 6, 2 * n (where n is the integer input representing the size of the n × n matrix)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: The output consists of 2 * n lines, with each line being either "1 i n (n-1) ... 2 1" or "2 i n (n-1) ... 2 1" for i ranging from 1 to n.
#Overall this is what the function does:The function `func_1` reads an integer `n` representing the size of an n × n matrix and prints a specific sequence of lines. For each test case, it prints the value `n * (n + 1) * (4 * n - 1) // 6` followed by `2 * n`, and then outputs `2 * n` lines, each consisting of either "1 i n (n-1) ... 2 1" or "2 i n (n-1) ... 2 1" for i ranging from 1 to n.

