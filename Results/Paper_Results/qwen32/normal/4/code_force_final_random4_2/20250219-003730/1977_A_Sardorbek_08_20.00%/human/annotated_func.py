#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. Each of the following t lines contains two integers n and m such that 1 <= n, m <= 100.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        q = b, c
        
        if b == c:
            print('YES')
        elif b < c:
            print('NO')
        elif a % 2 == b % 2:
            print('Yes')
        else:
            print('No')
        
    #State: `t` is an integer such that 1 <= t <= 100, each of the following t lines contains two integers `n` and `m` such that 1 <= n, m <= 100, `a` is the number of iterations, `i` is equal to `a`, `b` and `c` are the integers read in the last iteration, and `q` is the tuple `(b, c)` from the last iteration.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `m`. It then prints 'YES' if `n` is equal to `m`, 'NO' if `n` is less than `m`, and checks if both `n` and `m` are either even or odd to print 'Yes' or 'No' accordingly.

