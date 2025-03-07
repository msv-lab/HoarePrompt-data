#State of the program right berfore the function call: The function `func_1` does not take any input parameters, but it is expected to handle multiple test cases. Each test case contains a single integer n (1 ≤ n ≤ 500) representing the size of the n×n matrix. The number of test cases t (1 ≤ t ≤ 500) is provided in the input, and the sum of n^2 over all test cases does not exceed 5 \cdot 10^5.
def func_1():
    n = int(input())
    print(n * (n + 1) * (4 * n - 1) // 6, 2 * n)
    #This is printed: n * (n + 1) * (4 * n - 1) // 6, 2 * n (where n is the integer input by the user)
    for i in range(1, n + 1):
        print(1, i, *range(n, 0, -1))
        
        print(2, i, *range(n, 0, -1))
        
    #State: The value of `n` remains unchanged, and `t` (the number of test cases) also remains unchanged. The loop prints two lines for each value of `i` from 1 to `n`, where the first line starts with `1` followed by `i` and then the integers from `n` to `1` in descending order, and the second line starts with `2` followed by `i` and then the integers from `n` to `1` in descending order.
#Overall this is what the function does:The function `func_1` reads an integer `n` from the user input, prints a tuple containing the values `n * (n + 1) * (4 * n - 1) // 6` and `2 * n`, and then prints two lines for each integer `i` from 1 to `n`. Each line starts with either `1` or `2`, followed by `i`, and then the integers from `n` to `1` in descending order. The function does not return any value and does not modify the input or any external state.

