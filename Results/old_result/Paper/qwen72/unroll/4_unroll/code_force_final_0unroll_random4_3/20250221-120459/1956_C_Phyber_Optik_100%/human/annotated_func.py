#State of the program right berfore the function call: The function does not take any input parameters. However, based on the problem description, it is implied that the function should be called within a loop that processes multiple test cases, where each test case provides an integer n (1 ≤ n ≤ 500) representing the size of the matrix.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum = 1
        
        for i in range(2, n + 1):
            sum += (i * i - (i - 1) * (i - 1)) * i
        
        print(sum, n + n)
        
        for j in range(1, n + 1):
            print(1, n - j + 1, *range(1, n + 1))
            print(2, n - j + 1, *range(1, n + 1))
        
    #State: The loop will execute `t` times. In each iteration, `n` is read from the input, and the variable `sum` is calculated as the sum of the series `(i * i - (i - 1) * (i - 1)) * i` for `i` from 2 to `n`. The value of `sum` and `2 * n` are printed. Then, for each `j` from 1 to `n`, two lines are printed: the first line starts with `1` and `n - j + 1` followed by the range from 1 to `n`, and the second line starts with `2` and `n - j + 1` followed by the range from 1 to `n`. After all iterations, the values of `t` and `n` remain unchanged, but the output will include the printed values for each iteration.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `t` from the input, which represents the number of test cases. For each test case, it reads another integer `n` (1 ≤ n ≤ 500) representing the size of a matrix. The function calculates a sum based on a series and prints the sum along with `2 * n`. It then prints a series of lines for each `j` from 1 to `n`, where each line starts with either `1` or `2`, followed by `n - j + 1` and the range from 1 to `n`. After processing all test cases, the function does not return any value, but it produces the specified output for each test case. The values of `t` and `n` remain unchanged after the function execution.

