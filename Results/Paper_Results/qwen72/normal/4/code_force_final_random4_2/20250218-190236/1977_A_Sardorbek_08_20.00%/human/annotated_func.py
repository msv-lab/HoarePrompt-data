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
        
    #State: `t` is an integer such that 1 <= t <= 100, `n` and `m` are integers such that 1 <= n, m <= 100, `a` is an integer such that 0 <= a <= 100, `i` is `a` - 1, and `q` is a tuple containing the final values of `b` and `c`. For each iteration of the loop, the values of `b` and `c` were provided by user input, and the loop checked the conditions: if `b` == `c`, it printed 'YES'; if `b` < `c`, it printed 'NO'; if `a` and `b` have the same parity, it printed 'Yes'; otherwise, it printed 'No'. After all iterations, the loop has completed `a` times, and the variables `t`, `n`, and `m` remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `a` from user input, and for each integer from 0 to `a-1`, it reads two integers `b` and `c` from user input. It then checks the following conditions for each pair of `b` and `c`: if `b` equals `c`, it prints 'YES'; if `b` is less than `c`, it prints 'NO'; if `a` and `b` have the same parity (both even or both odd), it prints 'Yes'; otherwise, it prints 'No'. The function does not return any value, and the variables `t`, `n`, and `m` mentioned in the annotations are not used or modified by the function. After the function concludes, `a` will be an integer between 0 and 100, and `q` will be a tuple containing the last values of `b` and `c` that were read.

