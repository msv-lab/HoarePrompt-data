#State of the program right berfore the function call: t is an integer where 1 <= t <= 100, and for each test case, n and m are integers where 1 <= n, m <= 100.
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
        
    #State: The values of t, n, and m remain unchanged. The loop iterates a times, and for each iteration, it reads two integers b and c from the input. Depending on the values of b and c, it prints 'YES', 'NO', 'Yes', or 'No'. The variable a is not modified by the loop.
#Overall this is what the function does:The function `func` reads an integer `a` from the input, which represents the number of test cases. For each of the `a` test cases, it reads two integers `b` and `c` from the input. It then prints 'YES' if `b` is equal to `c`, 'NO' if `b` is less than `c`, 'Yes' if `a` and `b` have the same parity (both even or both odd), and 'No' otherwise. The function does not modify the values of `t`, `n`, or `m` mentioned in the preconditions, and it does not return any value. The final state of the program after the function concludes is that `a` test cases have been processed and the corresponding results have been printed.

