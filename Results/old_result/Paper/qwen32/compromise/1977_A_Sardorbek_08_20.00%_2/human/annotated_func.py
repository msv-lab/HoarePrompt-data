#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each of the t test cases, n and m are integers such that 1 <= n, m <= 100.
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
        
    #State: `a` is the same as the initial input integer, `b` and `c` are the integers from the last iteration of the loop, and `q` is the tuple `(b, c)` from the last iteration. The variables `t`, `n`, and `m` remain unchanged.
#Overall this is what the function does:The function reads an integer `a` representing the number of test cases. For each test case, it reads two integers `b` and `c`. It then prints 'YES' if `b` is equal to `c`, 'NO' if `b` is less than `c`, and checks if `a` and `b` have the same parity (both even or both odd) to print 'Yes' or 'No' accordingly.

