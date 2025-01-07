#State of the program right berfore the function call: a, b, and c are integers such that -10^9 ≤ a, b, c ≤ 10^9.
def func():
    a, b, c = map(int, input().split())
    if (b == a) :
        print('YES')
    else :
        if (c == 0) :
            print('NO')
        else :
            if ((b - a) % c == 0 and (b - a) / c >= 0) :
                print('YES')
            else :
                print('NO')
            #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers based on user input; `b` is not equal to `a`, and `c` is not equal to 0. If `(b - a)` is divisible by `c` and `(b - a) / c` is greater than or equal to 0, the output is 'YES'. Otherwise, the output is 'NO'.
        #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers based on user input, with `b` not equal to `a`. If `c` is equal to 0, 'NO' is printed to the console. If `c` is not equal to 0, then if `(b - a)` is divisible by `c` and `(b - a) / c` is greater than or equal to 0, 'YES' is printed. Otherwise, 'NO' is printed.
    #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers based on user input. If `b` is equal to `a`, then the program does not perform any action. If `b` is not equal to `a` and `c` is equal to 0, 'NO' is printed. If `c` is not equal to 0, then if `(b - a)` is divisible by `c` and `(b - a) / c` is greater than or equal to 0, 'YES' is printed. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function accepts three integers `a`, `b`, and `c` from user input. It prints 'YES' if `b` is equal to `a`. If `b` is not equal to `a` and `c` is zero, it prints 'NO'. If `c` is not zero, it checks if `(b - a)` is divisible by `c` and if the result of `(b - a) / c` is non-negative; it prints 'YES' if both conditions are met, otherwise it prints 'NO'.

