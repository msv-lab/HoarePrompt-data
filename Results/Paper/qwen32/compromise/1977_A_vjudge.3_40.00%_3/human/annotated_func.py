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
        
    #State: A series of 'Yes' or 'No' messages printed for each iteration based on the input pairs (n, m).
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers `n` and `m`. For each test case, it prints 'Yes' if certain conditions are met (either `n` equals `m`, `m` is exactly one less than `n`, or both `m` and `n` are either even or odd), and 'No' otherwise.

