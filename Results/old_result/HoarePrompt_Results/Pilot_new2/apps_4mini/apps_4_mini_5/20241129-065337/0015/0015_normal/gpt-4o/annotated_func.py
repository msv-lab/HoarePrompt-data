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
            #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers with `-10^9 ≤ a, b, c ≤ 10^9`, `b` is not equal to `a`, and `c` is not equal to 0. If `(b - a) % c == 0` and `(b - a) / c >= 0`, the output is 'YES'. Otherwise, if either `(b - a) % c != 0` or `(b - a) / c < 0`, the output is 'NO'.
        #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers with `-10^9 ≤ a, b, c ≤ 10^9`, and `b` is not equal to `a`. If `c` is 0, the execution reflects that `c` is currently 0. Otherwise, if `c` is not equal to 0, the output is 'YES' if `(b - a) % c == 0` and `(b - a) / c >= 0`, otherwise, the output is 'NO'.
    #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers with `-10^9 ≤ a, b, c ≤ 10^9`. If `b` is equal to `a`, 'YES' is printed to the console. If `b` is not equal to `a` and `c` is 0, it reflects that `c` is currently 0. If `c` is not equal to 0, 'YES' is printed if `(b - a) % c == 0` and `(b - a) / c >= 0`, otherwise 'NO' is printed.
#Overall this is what the function does:The function accepts three integers `a`, `b`, and `c` through user input. It prints 'YES' if `b` is equal to `a`. If `c` is 0 and `b` is not equal to `a`, it prints 'NO'. If `c` is not equal to 0, it checks if the difference `(b - a)` is divisible by `c` and non-negative; if both conditions are met, it prints 'YES', otherwise, it prints 'NO'. This function handles edge cases where `c` is zero and checks for divisibility and non-negativity in relation to the difference between `b` and `a`.

