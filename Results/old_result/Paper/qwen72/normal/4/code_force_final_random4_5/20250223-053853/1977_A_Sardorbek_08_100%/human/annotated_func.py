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
        
    #State: The loop has executed `a` times. For each iteration, the values of `b` and `c` were read from input, and a corresponding 'YES', 'NO', 'Yes', or 'No' was printed based on the conditions. The values of `t`, `n`, and `m` remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `a` from the user input, which represents the number of test cases. For each test case, it reads two integers `b` and `c` from the user input. It then prints 'YES' if `b` is equal to `c`, 'NO' if `b` is less than `c`, 'Yes' if `b` and `c` have the same parity (both even or both odd), and 'No' otherwise. The function does not return any value and does not modify any external variables. After the function concludes, `a` test cases have been processed, and the corresponding results have been printed for each case.

