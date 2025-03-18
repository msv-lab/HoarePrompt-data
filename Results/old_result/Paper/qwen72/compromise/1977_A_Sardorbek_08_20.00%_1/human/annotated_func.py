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
        elif a % 2 == b % 2:
            print('Yes')
        else:
            print('No')
        
    #State: The loop has executed `a` times. The final values of `b` and `c` are the last pair of integers read from the input, and the tuple `q` contains these final values. The values of `n` and `m` remain unchanged.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `a` from the input, and for each of the `a` iterations, it reads a pair of integers `b` and `c`. For each pair, it prints 'YES' if `b` equals `c`, 'NO' if `b` is less than `c`, and 'Yes' if `a` and `b` have the same parity (both even or both odd). If none of these conditions are met, it prints 'No'. The final state of the program after the function concludes is that the loop has executed `a` times, and the last values of `b` and `c` are stored in the tuple `q`. The function does not modify or use any external parameters `n` and `m`.

