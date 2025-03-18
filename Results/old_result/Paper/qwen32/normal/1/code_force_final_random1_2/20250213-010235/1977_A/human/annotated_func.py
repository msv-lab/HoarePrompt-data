#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. Each of the next t lines contains two integers n and m such that 1 ≤ n, m ≤ 100.
def func():
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()]
        
        if n == m:
            print('Yes')
        elif m > n:
            print('No')
        elif m == n - 1:
            print('Yes')
        elif m % 2 == 0 and n % 2 == 0:
            print('Yes')
        elif m % 2 != 0 and n % 2 != 0:
            print('Yes')
        else:
            print('No')
        
    #State: The loop has completed all `t` iterations. The variable `i` is equal to `t`, indicating that all test cases have been processed. The variables `n` and `m` hold the values from the last test case processed. The program has printed 'Yes' or 'No' for each of the `t` test cases based on the given conditions.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `m`. It then prints 'Yes' or 'No' based on specific conditions related to the values of `n` and `m`. After processing all test cases, the function concludes without returning any value.

