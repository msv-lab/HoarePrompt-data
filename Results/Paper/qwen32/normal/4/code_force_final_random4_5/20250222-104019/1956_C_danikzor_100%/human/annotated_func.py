#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 500) representing the number of test cases. Each of the following t lines contains a single integer n (1 ≤ n ≤ 500) representing the size of the matrix a for that test case. The sum of n^2 over all test cases does not exceed 5 \cdot 10^5.
def func_1():
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: n * (n + 1) * (4 * n - 1) // 6, 2 * n (where n is the number of test cases)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: i = n + 1
#Overall this is what the function does:The function `func_1` reads an integer `t` from standard input, representing the number of test cases. For each test case, it reads an integer `n` and then prints a specific sequence of numbers related to `n`. The function prints a calculated value based on `n` followed by a series of lines for each `i` from 1 to `n`, each containing two sequences of numbers.

