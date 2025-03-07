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
        elif a % 2 == b % 2:
            print('Yes')
        else:
            print('No')
        
    #State: `t` is an integer such that 1 <= t <= 100, `n` and `m` are integers such that 1 <= n, m <= 100, `a` is greater than or equal to 0, `i` is `a` (the final value of `i` is equal to `a`), `b` and `c` are the last input integers, and `q` is a tuple containing the values (`b`, `c`). If `b` == `c`, then `b` is equal to `c`. If `b` < `c`, then `b` is less than `c`. If `b` >= `c`, then `b` is greater than or equal to `c` and `b` is not equal to `c`. Additionally, if `a % 2` is equal to `b % 2`, then `a % 2` is equal to `b % 2`. If `a % 2` is not equal to `b % 2`, then `a % 2` is not equal to `b % 2.
#Overall this is what the function does:The function `func` reads an integer `a` from the user, and then for each of the `a` test cases, it reads two integers `b` and `c`. For each test case, it prints 'YES' if `b` equals `c`, 'NO' if `b` is less than `c`, and 'Yes' if `a` and `b` have the same parity (both are even or both are odd). Otherwise, it prints 'No'. After the function concludes, `a` is the number of test cases processed, `b` and `c` are the last input integers, and `q` is a tuple containing the last values of `b` and `c`.

