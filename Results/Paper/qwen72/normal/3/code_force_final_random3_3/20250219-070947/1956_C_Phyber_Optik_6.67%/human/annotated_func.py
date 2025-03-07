#State of the program right berfore the function call: The function does not take any input parameters. The problem description implies that the function should handle multiple test cases, each with an integer n (1 ≤ n ≤ 500) representing the size of an n×n matrix. The number of test cases t is also an integer (1 ≤ t ≤ 500). The function should be able to read these inputs from standard input and output the results to standard output.
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
        
    #State: `_` is `t - 1`, `n` is the last input integer, `i` is `n`, `sum` is the total sum of `n * (n + 1) // 2` for all `i` where `n * (n + 1) // 2 > i * n` plus the total sum of `i * n` for all `i` where `n * (n + 1) // 2 <= i * n` for the last test case, `r` is the largest integer `i` such that `n * (n + 1) // 2 > i * n` for the last test case, and `j` is `n + r + 1`.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case includes an integer `n` (1 ≤ n ≤ 500). For each test case, it calculates a sum based on the conditions provided and prints the sum along with `n + r`, where `r` is determined during the calculation. It then prints a series of lines, each containing a number (1 or 2), a second number (based on `j`), and a sequence of numbers from 1 to `n`. After processing all test cases, the function completes and the final state includes the last processed `n`, the sum calculated for the last test case, and the value of `r` for the last test case.

