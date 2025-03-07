#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 500) representing the number of test cases. Each of the following t lines contains a single integer n (1 ≤ n ≤ 500) representing the size of the matrix for that test case. It is guaranteed that the sum of n^2 over all test cases does not exceed 5 · 10^5.
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
        
    #State: - Since `t = 2`, there are two test cases.
    #   - We already have the states for both test cases.
    #   - The final output state will be the state after the second test case.
    #
    #Given the above analysis, the final output state after all iterations is:
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the size of a matrix. For each test case, it calculates and prints a sum and a value `n + r`, followed by a series of lines describing operations on the matrix. The final state of the program after processing all test cases is the output of the calculated sums, values, and matrix operations for each test case.

