#State of the program right berfore the function call: Each test case contains an integer n (1 ≤ n ≤ 500) representing the size of the n × n matrix filled with zeroes. The function should handle multiple test cases, where the total number of test cases t is between 1 and 500, and the sum of n^2 over all test cases does not exceed 5 × 10^5.
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
        
    #State: t is the number of test cases, n is the size of the matrix for the last test case, sum is the cumulative sum calculated for the last test case, r is the largest i for which n * (n + 1) // 2 > i * n holds true for the last test case, and j is n + r + 1. The loop has completed all iterations, with j having taken on all values from 1 to n + r + 1 for the last test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by an integer `n` representing the size of an `n × n` matrix. For each test case, it calculates and prints a specific sum and a series of matrix operations. The sum is derived based on a conditional logic involving the triangular number sequence and the size `n`. The matrix operations involve printing a sequence of commands to manipulate an `n × n` matrix, filling it with values in a specific pattern.

