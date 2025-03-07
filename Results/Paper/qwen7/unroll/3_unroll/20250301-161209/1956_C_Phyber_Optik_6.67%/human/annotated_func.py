#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n^2 over all test cases does not exceed 5 × 10^5.
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
        
    #State: Output State: The output state will consist of multiple lines, each corresponding to one iteration of the outer loop. For each iteration, there will be two lines:
    #
    #1. The first line contains two integers: the value of `sum` and `n + r`.
    #2. The second line contains either `n` or `n + r` lines, each representing a sequence of numbers. Each line starts with either `1` or `2`, followed by a space-separated list of numbers from `1` to `n`.
    #
    #For each iteration, `sum` is calculated based on the given logic, and `r` is determined by the condition in the inner loop. The exact values of `sum` and `r` depend on the input `n` for each iteration. The second part of the output generates a specific pattern of numbers based on the values of `n` and `r`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( t \) and \( n \). For each test case, it calculates a sum based on specific conditions and determines a value \( r \). It then prints the sum and \( n + r \) for each test case. Following this, it generates a pattern of numbers, printing either \( n \) or \( n + r \) lines, each starting with either `1` or `2` and followed by a sequence of numbers from `1` to \( n \). The function does not return any value but prints the results directly.

