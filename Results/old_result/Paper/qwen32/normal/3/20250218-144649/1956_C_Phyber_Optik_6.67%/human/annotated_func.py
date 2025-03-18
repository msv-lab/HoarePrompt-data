#State of the program right berfore the function call: Each test case contains an integer n (1 ≤ n ≤ 500) representing the size of the n × n matrix a filled with zeroes. The number of test cases t satisfies 1 ≤ t ≤ 500, and the sum of n^2 over all test cases does not exceed 5 × 10^5.
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
        
    #State: The final output state after all iterations is the concatenation of the output states for each test case, where each test case prints `sum` and `n + r`, followed by a sequence of commands based on `n` and `r`.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` representing the size of an `n × n` matrix. For each test case, it calculates a sum and a value `r`, then prints the sum and `n + r`. It also prints a sequence of commands that involve printing rows of the matrix. The function does not modify the matrix itself but outputs a series of commands that could be used to fill or manipulate the matrix.

