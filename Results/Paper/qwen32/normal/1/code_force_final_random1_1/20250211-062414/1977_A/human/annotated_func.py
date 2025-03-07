#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. Each of the next t lines contains two integers n and m such that 1 <= n, m <= 100.
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
        
    #State: The loop has completed `t` iterations, and for each pair `(n, m)`, "Yes" or "No" has been printed based on the specified conditions. The values of `t`, `n`, and `m` reflect the last pair processed.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `m`. Based on specific conditions related to the values of `n` and `m`, it prints "Yes" or "No".

