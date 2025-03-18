#State of the program right berfore the function call: The function does not take any input parameters, but it is expected to handle multiple test cases where each test case contains a single integer n (1 ≤ n ≤ 500) representing the size of the matrix. The number of test cases t is an integer (1 ≤ t ≤ 500) and is provided in the input.
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
        
    #State: `t` is 0, `n` is the last positive integer input, `i` is `n + 1`, `j` is `n + r`, `r` is `n`, and `sum` is the total sum of `n * (n + 1) // 2` for all `i` where `n * (n + 1) // 2 > i * n`, plus the total sum of `i * n` for all `i` where `n * (n + 1) // 2 <= i * n` for each iteration.
#Overall this is what the function does:The function `func` does not accept any parameters but reads input from the user to handle multiple test cases. For each test case, it receives an integer `n` (1 ≤ n ≤ 500) representing the size of a matrix. The function computes a sum and a value `r` based on the input `n`, and prints the sum and `n + r`. It then prints a series of lines, each containing a type (1 or 2), a value, and a sequence of integers from 1 to `n`. After processing all test cases, the function concludes with `t` set to 0, `n` set to the last positive integer input, `i` set to `n + 1`, `j` set to `n + r`, `r` set to the last computed value, and `sum` set to the total computed sum for the last test case.

