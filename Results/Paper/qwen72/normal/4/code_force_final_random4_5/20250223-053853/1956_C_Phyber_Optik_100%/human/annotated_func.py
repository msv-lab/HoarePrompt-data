#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500, and for each test case, n is an integer such that 1 <= n <= 500.
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
        
    #State: The variable `t` remains an integer such that 1 <= t <= 500. For each test case, the variable `n` is an integer such that 1 <= n <= 500. The loop prints the value of `sum` and `2 * n` for each test case, followed by two lines of output for each `j` from 1 to `n`, each line containing `1` or `2`, `n - j + 1`, and a sequence of integers from 1 to `n`. The value of `sum` for each test case is calculated as the sum of `(i * i - (i - 1) * (i - 1)) * i` for `i` from 2 to `n`, and then printed along with `2 * n`.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `t` from the input, where `1 <= t <= 500`, representing the number of test cases. For each test case, it reads another integer `n` from the input, where `1 <= n <= 500`. It calculates a sum based on the formula `(i * i - (i - 1) * (i - 1)) * i` for `i` ranging from 2 to `n`, and prints this sum along with `2 * n`. Additionally, for each `j` from 1 to `n`, it prints two lines: the first line contains `1`, `n - j + 1`, and a sequence of integers from 1 to `n`, and the second line contains `2`, `n - j + 1`, and the same sequence of integers from 1 to `n`. After processing all test cases, the function concludes, and the variable `t` remains an integer such that `1 <= t <= 500`.

