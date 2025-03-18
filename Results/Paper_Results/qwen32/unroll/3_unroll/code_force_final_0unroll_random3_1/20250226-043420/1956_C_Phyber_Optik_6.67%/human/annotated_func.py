#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains an integer t (1 ≤ t ≤ 500) representing the number of test cases. Each test case consists of a single integer n (1 ≤ n ≤ 500) representing the size of the n x n matrix. The sum of n^2 over all test cases does not exceed 5 * 10^5.
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
        
    #State: `sum` and `r` will be in their final state after the last test case, and the output will consist of the print statements for each test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case is defined by an integer `n` representing the size of an `n x n` matrix. For each test case, it calculates and prints a specific sum and a sequence of operations involving the matrix size. The sum is derived based on a conditional logic related to the matrix size, and the sequence of operations involves printing indices and ranges up to `n + r`, where `r` is determined during the calculation. The function outputs the calculated sum and the sequence of operations for each test case.

