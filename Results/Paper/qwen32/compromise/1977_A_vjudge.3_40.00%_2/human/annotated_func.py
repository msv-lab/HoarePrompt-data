#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. Each of the following t lines contains two integers n and m such that 1 <= n, m <= 100.
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
        
    #State: A series of 'Yes' or 'No' responses, one for each pair of `n` and `m`, determined by the conditions specified in the loop.
#Overall this is what the function does:The function reads an integer `t`, followed by `t` pairs of integers (`n`, `m`). For each pair, it prints 'Yes' or 'No' based on specific conditions: 'Yes' if `n` equals `m`, `m` is exactly one less than `n`, or both `n` and `m` are even or both are odd; otherwise, it prints 'No'.

