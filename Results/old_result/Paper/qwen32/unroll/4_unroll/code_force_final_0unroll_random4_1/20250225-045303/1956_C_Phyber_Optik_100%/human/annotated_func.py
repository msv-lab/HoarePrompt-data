#State of the program right berfore the function call: Each test case contains an integer n (1 ≤ n ≤ 500) representing the size of the n × n matrix a filled with zeroes. The function should handle multiple test cases, with the total number of test cases t (1 ≤ t ≤ 500) and the sum of n^2 over all test cases not exceeding 5 × 10^5.
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
        
    #State: After processing all test cases, the program will have printed the results for each test case. Each test case will output the sum calculated in the loop and the value n + n, followed by 2n lines describing specific row operations on an n × n matrix filled with zeroes. The state of the input variable `t` and the loop counter `_` will not be preserved as they are local to the loop. The variable `n` will hold the value of the last test case processed, and the variable `sum` will hold the sum calculated for that last test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the size of an `n × n` matrix filled with zeroes. For each test case, it calculates a specific sum based on the formula provided and prints this sum along with `2n`. It then prints `2n` lines, each describing row operations on the matrix.

