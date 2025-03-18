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
        
    #State: The variable `a` is decremented to 0 after all iterations of the loop have completed. The variables `t`, `n`, and `m` remain unchanged as they are not modified within the loop. For each iteration, the loop reads two integers `b` and `c` from input, and prints 'YES' if `b` equals `c`, 'NO' if `b` is less than `c`, 'Yes' if `b` and `c` have the same parity (both even or both odd), and 'No' otherwise. The variables `b`, `c`, and `q` are updated in each iteration but their final values are not retained after the loop completes.
#Overall this is what the function does:The function `func` does not accept any parameters. It reads an integer `a` from the user input, which represents the number of test cases. For each test case, it reads two integers `b` and `c` from the user input. It then prints 'YES' if `b` equals `c`, 'NO' if `b` is less than `c`, 'Yes' if `b` and `c` have the same parity (both even or both odd), and 'No' otherwise. After processing all test cases, the function does not return any value. The variables `t`, `n`, and `m` (if they exist) remain unchanged as they are not modified within the function. The variables `b`, `c`, and `q` are updated in each iteration but their final values are not retained after the loop completes.

