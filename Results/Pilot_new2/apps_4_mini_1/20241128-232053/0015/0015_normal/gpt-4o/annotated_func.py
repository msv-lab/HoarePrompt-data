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
            #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers input by the user, with `b` not equal to `a`, and `c` not equal to 0. If the difference between `b` and `a` is divisible by `c` and the result of the division `(b - a) / c` is greater than or equal to 0, then 'YES' is printed. Otherwise, if the difference is not divisible by `c` or the result of the division is less than 0, 'NO' is printed.
        #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers input by the user, with `b` not equal to `a`. If `c` is 0, no further actions are taken. If `c` is not 0, 'YES' is printed if the difference between `b` and `a` is divisible by `c` and the result of the division `(b - a) / c` is greater than or equal to 0; otherwise, 'NO' is printed.
    #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers input by the user. If `b` is equal to `a`, 'YES' is printed. If `b` is not equal to `a` and `c` is 0, no further actions are taken. If `c` is not 0, 'YES' is printed if the difference between `b` and `a` is divisible by `c` and the result of the division `(b - a) / c` is greater than or equal to 0; otherwise, 'NO' is printed.
#Overall this is what the function does:The function accepts no parameters directly, but reads three integers `a`, `b`, and `c` from user input. It prints 'YES' if `b` is equal to `a`. If `b` is not equal to `a` and `c` is zero, it prints 'NO'. If `c` is not zero, it checks if the difference `(b - a)` is divisible by `c` and if the result of the division `(b - a) / c` is non-negative; it prints 'YES' if both conditions are met, otherwise it prints 'NO'.

