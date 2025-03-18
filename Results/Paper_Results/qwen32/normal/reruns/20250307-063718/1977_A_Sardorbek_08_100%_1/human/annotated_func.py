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
        
    #State: `t` is an integer such that 1 <= t <= 100, `n` and `m` are integers such that 1 <= n, m <= 100, `a` is greater than 0, `b` and `c` are the integers provided by the input, `q` is the tuple `(b, c)`. If `b` equals `c`, then `b` is equal to `c`. Otherwise, `b` is not equal to `c`, and if `b` is less than `c`, then `b` is indeed less than `c`. If `b` is greater than or equal to `c`, then `b` is greater than or equal to `c`, and `b % 2` equals `c % 2` if and only if `b % 2` equals `c % 2`. `i` is `a - 1`.
#Overall this is what the function does:The function reads an integer `a` representing the number of test cases. For each test case, it reads two integers `b` and `c`. It then prints 'YES' if `b` equals `c`, 'NO' if `b` is less than `c`, and 'Yes' if `b` is greater than or equal to `c` and both `b` and `c` have the same parity (both even or both odd). Otherwise, it prints 'No'.

