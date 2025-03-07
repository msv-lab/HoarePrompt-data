#State of the program right berfore the function call: The function does not take any input parameters, but it is expected to handle multiple test cases. Each test case contains a single integer n (1 ≤ n ≤ 500) representing the size of the n×n matrix. The number of test cases t is also given, with 1 ≤ t ≤ 500, and the sum of n^2 over all test cases does not exceed 5⋅10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum, r = 0, 0
        
        for i in range(1, n + 1):
            if n * (n + 1) // 2 > i * n:
                r = i
                sum += n * (n + 1) // 2
            else:
                sum += i * n
        
        print(sum, n + r)
        
        for j in range(1, n + r + 1):
            if j <= n:
                print(1, j, end=' ')
                print(*range(1, n + 1))
            else:
                print(2, j % n, end=' ')
                print(*range(1, n + 1))
        
    #State: After all iterations, `t` is 0, `_` is `t`, `n` is the last input integer, `sum` is the total sum of `n * (n + 1) // 2` for each iteration where `n * (n + 1) // 2 > i * n`, and the total sum of `i * n` for each iteration where `n * (n + 1) // 2 <= i * n` for all test cases, `r` is the last value of `i` for which `n * (n + 1) // 2 > i * n` for the last test case, and `j` is `n + r` for the last test case.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it takes an integer `n` (1 ≤ n ≤ 500) representing the size of an n×n matrix. It calculates a sum and a value `r` based on the condition `n * (n + 1) // 2 > i * n` for each integer `i` from 1 to `n`. The function then prints the calculated sum and `n + r`. Following this, it prints a series of lines for each integer `j` from 1 to `n + r`. If `j` is less than or equal to `n`, it prints `1` followed by `j` and the integers from 1 to `n`. If `j` is greater than `n`, it prints `2` followed by `j % n` and the integers from 1 to `n`. After processing all test cases, the function completes without returning any value.

