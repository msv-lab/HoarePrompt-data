#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each test case, n and m are integers such that 1 <= n, m <= 100.
def func():
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        q = b, c
        
        if b == c:
            print('YES')
        elif b < c:
            print('NO')
        elif b % 2 == c % 2:
            print('Yes')
        else:
            print('No')
        
    #State: `t` is an integer such that 1 <= t <= 100, `n` and `m` are integers such that 1 <= n, m <= 100, `a` is an integer such that 1 <= a <= 100, `i` is `a-1`, `b` and `c` are input integers, `q` is the tuple `(b, c)`. For each iteration, if `b` is equal to `c`, then `b` remains equal to `c`. If `b` is less than `c`, then `b` remains less than `c`. If `b` and `c` have the same parity (both even or both odd), then `b` and `c` maintain their initial relationship (either `b` is equal to `c`, `b` is less than `c`, or `b` is greater than or equal to `c`). If `b` and `c` have different parities, then `b` and `c` also maintain their initial relationship (either `b` is equal to `c`, `b` is less than `c`, or `b` is greater than or equal to `c`).
#Overall this is what the function does:The function `func` reads an integer `a` from the user, which represents the number of test cases. For each test case, it reads two integers `b` and `c` from the user. It then prints 'YES' if `b` is equal to `c`, 'NO' if `b` is less than `c`, and 'Yes' if `b` and `c` have the same parity (both even or both odd). If `b` and `c` have different parities, it prints 'No'. After processing all test cases, the function does not return any value. The final state of the program includes the variables `a`, `i`, `b`, `c`, and `q`, where `a` is the number of test cases, `i` is `a-1`, and `q` is the tuple `(b, c)` from the last test case. The variables `b` and `c` maintain their initial relationships (equal, less than, or greater than) and parities throughout the function execution.

