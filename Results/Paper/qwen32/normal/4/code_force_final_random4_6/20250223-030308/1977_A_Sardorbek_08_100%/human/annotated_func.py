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
        
    #State: `t` is an integer such that 1 <= t <= 100, `n` and `m` are integers such that 1 <= n, m <= 100, `a` is an integer representing the number of iterations, `i` is equal to `a` (indicating the loop has finished all iterations), and `b` and `c` are the last pair of integers read from the input. The variable `q` is the tuple `(b, c)` from the last iteration. The state of `t`, `n`, and `m` remains unchanged as they are not affected by the loop.
#Overall this is what the function does:The function reads an integer `a` representing the number of test cases. For each test case, it reads two integers `b` and `c`. It then prints 'YES' if `b` equals `c`, 'NO' if `b` is less than `c`, 'Yes' if `b` and `c` have the same parity (both even or both odd), and 'No' otherwise. The function does not return any value; it only prints the results for each test case.

