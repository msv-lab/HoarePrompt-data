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
        elif a % 2 == b % 2:
            print('Yes')
        else:
            print('No')
        
    #State: Output State: `t` is a positive integer such that \(1 \leq t \leq 100\), `a` is an input integer, `i` is equal to `a`, `b` is the last integer obtained from the input split, `c` is the last integer obtained from the second input split, `q` is a tuple containing `b` and `c`. The value of `t` remains unchanged, and the loop has completed all its iterations based on the input value of `a`.
    #
    #This means that after the loop has executed all its iterations, the variable `i` will be equal to `a`, indicating that the loop has run exactly `a` times. The values of `b` and `c` will be the last pair of integers entered by the user during the final iteration of the loop. The variable `t` remains within the range \(1 \leq t \leq 100\) and does not change throughout the loop's execution.
#Overall this is what the function does:The function processes a series of test cases defined by an integer `a`. For each test case, it reads two integers `b` and `c`, then prints 'YES' if `b` equals `c`, 'NO' if `b` is less than `c`, and 'Yes' if both `b` and `a` have the same parity (both even or both odd). After processing all test cases, the function does not return any value.

