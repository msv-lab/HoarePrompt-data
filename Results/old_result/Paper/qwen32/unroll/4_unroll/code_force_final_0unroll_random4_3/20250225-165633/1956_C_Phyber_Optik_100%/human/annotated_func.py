#State of the program right berfore the function call: Each test case contains a single integer n (1 ≤ n ≤ 500) representing the size of the n × n matrix a. The number of test cases t (1 ≤ t ≤ 500) is given at the start, and the sum of n^2 over all test cases does not exceed 5 · 10^5.
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
        
    #State: a sequence of outputs for each test case, where each output includes the calculated `sum` and `2 * n`, followed by `n` pairs of lines as described in the code.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` representing the size of an `n × n` matrix. For each test case, it calculates a specific `sum` based on the formula provided and prints this `sum` along with `2 * n`. It then prints `n` pairs of lines, each pair consisting of two lines that describe specific patterns involving the matrix's dimensions and indices.

