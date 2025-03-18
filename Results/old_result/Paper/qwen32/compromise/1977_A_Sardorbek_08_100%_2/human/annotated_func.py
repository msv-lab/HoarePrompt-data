#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, and for each of the t test cases, there are two integers n and m such that 1 <= n, m <= 100.
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
        
    #State: t is an integer such that 1 <= t <= 100, and for each of the t test cases, there are two integers n and m such that 1 <= n, m <= 100; a is an input integer. The loop has printed a series of 'YES', 'NO', 'Yes', or 'No' based on the comparisons of b and c for each of the a iterations.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `m`. It then prints 'YES' if `n` is equal to `m`, 'NO' if `n` is less than `m`, 'Yes' if `n` and `m` have the same parity (both even or both odd), and 'No' otherwise.

