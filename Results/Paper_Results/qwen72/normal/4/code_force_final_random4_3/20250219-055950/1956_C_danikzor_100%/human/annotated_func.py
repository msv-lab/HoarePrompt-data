#State of the program right berfore the function call: The function `func_1` does not take any input parameters, but it is expected to handle multiple test cases. Each test case contains a single integer `n` (1 ≤ n ≤ 500) representing the size of the matrix. The number of test cases `t` is also given (1 ≤ t ≤ 500), and the sum of `n^2` over all test cases does not exceed 5 · 10^5.
def func_1():
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: [n * (n + 1) * (4 * n - 1) // 6], [2 * n] (where n is the input integer between 1 and 500, inclusive)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: `n` is an input integer between 1 and 500, inclusive; the number of test cases `t` is still given (1 ≤ t ≤ 500), and the sum of `n^2` over all test cases does not exceed 5 · 10^5, `i` is `n`, `n` must be greater than or equal to `n`.
#Overall this is what the function does:The function `func_1` reads an integer `n` from the input, where `n` is between 1 and 500 inclusive. It then prints two values: the first is the result of the formula `n * (n + 1) * (4 * n - 1) // 6`, and the second is `2 * n`. Following this, it prints a series of lines for each integer `i` from 1 to `n`, inclusive. Each line consists of two parts: the first part is `1, i,` followed by a descending sequence of integers from `n` to 1, and the second part is `2, i,` followed by the same descending sequence. The function does not return any values; all output is printed to the console. The function is designed to handle multiple test cases, but it processes only one test case per call.

