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
        
    #State: t remains an integer such that 1 <= t <= 100, and for each test case, n and m are integers such that 1 <= n, m <= 100; a is an input integer. The loop has executed a times, and for each iteration, it has printed 'YES' if b == c, 'NO' if b < c, 'Yes' if b % 2 == c % 2, and 'No' otherwise. The values of b, c, and q are not retained after the loop finishes.
#Overall this is what the function does:The function `func` reads an integer `a` from the input, which represents the number of test cases. For each test case, it reads two integers `b` and `c` from the input. It then checks the following conditions for each test case: if `b` is equal to `c`, it prints 'YES'; if `b` is less than `c`, it prints 'NO'; if `b` and `c` have the same parity (both even or both odd), it prints 'Yes'; otherwise, it prints 'No'. After processing all test cases, the function does not return any value, and the values of `b`, `c`, and `q` are not retained. The function does not modify any external state or variables outside its scope.

