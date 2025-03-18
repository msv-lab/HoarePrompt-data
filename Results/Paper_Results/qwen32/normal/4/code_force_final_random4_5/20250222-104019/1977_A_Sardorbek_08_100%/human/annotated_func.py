#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n and m are integers such that 1 <= n, m <= 100.
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
        
    #State: `t` is an integer such that 1 <= t <= 100; `n` and `m` are integers such that 1 <= n, m <= 100; `a` is greater than or equal to 1; `b` and `c` are integers provided by the input; `q` is a tuple containing the values of `b` and `c` from the last iteration; If `b` equals `c`, then `b` is equal to `c`. Otherwise, `b` is not equal to `c`; If `b < c`, `b` is less than `c`; If `b` and `c` have the same parity (both even or both odd), then `b` and `c` have the same parity; otherwise, they have different parities; `i` is equal to `a` (the loop has finished all iterations).
#Overall this is what the function does:The function reads an integer `a` representing the number of test cases. For each test case, it reads two integers `b` and `c`. It then prints "YES" if `b` is equal to `c`, "NO" if `b` is less than `c`, and "Yes" if `b` and `c` have the same parity (both even or both odd). Otherwise, it prints "No".

