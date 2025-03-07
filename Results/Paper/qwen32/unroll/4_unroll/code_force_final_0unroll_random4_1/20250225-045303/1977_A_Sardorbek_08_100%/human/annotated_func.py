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
        
    #State: t is an integer such that 1 <= t <= 100; n and m are integers such that 1 <= n, m <= 100; a is an input integer.
#Overall this is what the function does:The function reads an integer `a` representing the number of test cases. For each test case, it reads two integers `b` and `c`. It then prints 'YES' if `b` equals `c`, 'NO' if `b` is less than `c`, 'YES' if both `b` and `c` have the same parity (both even or both odd), and 'NO' otherwise.

