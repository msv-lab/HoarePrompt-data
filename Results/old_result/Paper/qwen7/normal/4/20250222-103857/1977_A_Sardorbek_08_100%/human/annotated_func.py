#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 100.
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
        
    #State: `t` is a positive integer such that \(1 \leq t \leq 100\), `a` is an input integer, `i` is equal to `a`, `b` is an integer from the input split, `c` is an integer from the input split, and `q` is a tuple containing (`b`, `c`). Regardless of the values of `b` and `c`, the value of `q` remains unchanged throughout the loop's execution.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers `b` and `c`. It checks if `b` equals `c`, if `b` is less than `c`, if `b` and `c` have the same parity (both even or both odd), and prints 'YES', 'NO', 'Yes', or 'No' based on these conditions. After processing all test cases, the function does not return any value.

