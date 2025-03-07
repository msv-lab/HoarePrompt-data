#State of the program right berfore the function call: The function `func` does not take any input parameters. However, based on the problem description, it is implied that the function should be able to handle multiple test cases, each with an integer n (1 ≤ n ≤ 500) representing the size of the matrix. The function should be designed to read input from stdin or another source, where the first line contains the number of test cases t (1 ≤ t ≤ 500), followed by t lines, each containing a single integer n.
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
        
    #State: After the loop executes all the iterations, the variable `t` will be unchanged, and the variables `n`, `sum`, and `r` will have been updated for each test case. For each test case, `n` will be the last input integer, `sum` will be the accumulated sum based on the conditions in the loop, and `r` will be the last value of `i` that satisfies the condition `n * (n + 1) // 2 > i * n`. The loop will print the final values of `sum` and `n + r` for each test case, followed by a series of printed lines for each value of `j` from 1 to `n + r`.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, where each test case consists of an integer `n` (1 ≤ n ≤ 500). For each test case, the function calculates a sum and a value `r` based on the conditions provided in the loop. It then prints the sum and the value `n + r`. Additionally, it prints a series of lines, each containing a row of the matrix, with the first element being either 1 or 2 depending on the value of `j` (1 to `n + r`). The function does not return any values; all results are printed to standard output.

