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
        
    #State: After all iterations of the loop, `sum` will contain the total sum calculated based on the conditions within the loop for all given `t` iterations. `j` will be `n + r + 1` for the last iteration, `n` will be 0, `t` will be 0 (since all iterations are completed), `r` will be the last value of `i` that satisfied the condition `n * (n + 1) // 2 > i * n` or 0 if no such `i` exists, and `i` will be `n` (which is 0).
#Overall this is what the function does:The function processes a series of test cases, each containing integers `t` and `n`. For each test case, it calculates a sum based on specific conditions involving `n` and prints the sum along with a sequence of numbers. After processing all test cases, it prints a series of sequences of numbers for each test case.

