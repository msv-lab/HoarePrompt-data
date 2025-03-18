#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each test case, there are two integers n and m such that 1 <= n, m <= 100.
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
        
    #State: `t` is an integer such that 1 <= t <= 100, `n` and `m` are integers such that 1 <= n, m <= 100, `a` is an integer such that a >= 1, `b` and `c` are integers read from the input during the last iteration, `q` is a tuple (`b`, `c`) from the last iteration, and `i` equals `a`.
#Overall this is what the function does:The function reads an integer `a` representing the number of test cases. For each test case, it reads two integers `b` and `c`. It then prints 'YES' if `b` equals `c`, 'NO' if `b` is less than `c`, and checks if both `a` and `b` have the same parity (both even or both odd) to print 'Yes' if true, otherwise 'No'.

