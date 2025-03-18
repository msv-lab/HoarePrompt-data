#State of the program right berfore the function call: a, b, and c are integers within the range of -10^9 to 10^9.
def func():
    a, b, c = map(int, input().split())
    if (c == 0) :
        if (a == b) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers. If `a` is equal to `b`, then 'YES' is printed. Otherwise, `a`, `b`, and `c` are integers with `c` equal to 0, and `a` is not equal to `b`.
    else :
        if ((b - a) % c == 0 and (b - a) / c >= 0) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers. If `(b - a) % c == 0` and `(b - a) / c >= 0`, then 'YES' is printed. Otherwise, if either `(b - a) % c` is not equal to 0 or `(b - a) / c` is less than 0, then 'NO' is printed.
    #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers. If `c` is equal to 0 and `a` is equal to `b`, then 'YES' is printed. Otherwise, if `c` is equal to 0 and `a` is not equal to `b`, nothing is printed. If `c` is not equal to 0, 'YES' is printed if `(b - a) % c == 0` and `(b - a) / c >= 0`. Otherwise, 'NO' is printed if either `(b - a) % c` is not equal to 0 or `(b - a) / c` is less than 0.
#Overall this is what the function does:The function accepts three integer inputs `a`, `b`, and `c` from the user. If `c` is equal to 0, it checks if `a` is equal to `b`; if they are equal, it prints 'YES', otherwise it prints 'NO'. If `c` is not equal to 0, it checks if the difference `(b - a)` is divisible by `c` and if the result of `(b - a) / c` is non-negative; if both conditions are met, it prints 'YES', otherwise it prints 'NO'. The function does not return any value.

