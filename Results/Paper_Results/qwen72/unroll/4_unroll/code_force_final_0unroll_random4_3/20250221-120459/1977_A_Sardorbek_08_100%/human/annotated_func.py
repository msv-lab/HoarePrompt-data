#State of the program right berfore the function call: The function should take two parameters, n and m, where n and m are integers such that 1 <= n, m <= 100.
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
        
    #State: The values of `a`, `n`, and `m` remain unchanged. The loop iterates `a` times, and during each iteration, it reads two integers `b` and `c` from the input. For each pair, it prints 'YES' if `b` equals `c`, 'NO' if `b` is less than `c`, 'Yes' if `b` and `c` have the same parity (both even or both odd), and 'No' otherwise. The variables `b`, `c`, and `q` are updated in each iteration but do not persist outside the loop.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `a` from the input, and for `a` iterations, it reads two integers `b` and `c` from the input. For each pair of integers, it prints 'YES' if `b` equals `c`, 'NO' if `b` is less than `c`, 'Yes' if `b` and `c` have the same parity (both even or both odd), and 'No' otherwise. The function does not modify any external state or variables outside of its scope.

