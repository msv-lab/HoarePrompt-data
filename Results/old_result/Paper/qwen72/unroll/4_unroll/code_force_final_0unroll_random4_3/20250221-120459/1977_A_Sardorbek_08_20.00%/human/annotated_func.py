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
        
    #State: The values of `t`, `n`, and `m` remain unchanged. The loop iterates `a` times, and for each iteration, it reads two integers `b` and `c` from input. Depending on the values of `b` and `c`, it prints 'YES', 'NO', 'Yes', or 'No' as specified in the loop body. The variables `b`, `c`, and `q` are updated in each iteration, but their final values after the loop are the values from the last iteration.
#Overall this is what the function does:The function `func` reads an integer `a` from the input, which represents the number of test cases. For each test case, it reads two integers `b` and `c` from the input. Depending on the values of `b` and `c`, it prints 'YES', 'NO', 'Yes', or 'No' to the console. The function does not return any value. The variables `b`, `c`, and `q` are updated in each iteration, but their final values after the loop are the values from the last iteration. The function does not modify the values of `t`, `n`, or `m` (if they exist outside the function).

