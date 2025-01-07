#State of the program right berfore the function call: a, b, and c are integers such that -10^9 ≤ a, b, c ≤ 10^9.
def func():
    a, b, c = map(int, input().split())
    if (c == 0) :
        if (a == b) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers assigned from input values. If `a` equals `b`, then 'YES' is printed, and the current value of `c` remains 0. Otherwise, if `a` is not equal to `b`, the current value of `c` is still 0.
    else :
        if ((b - a) % c == 0 and (b - a) / c >= 0) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers. Since `c` is not equal to 0, if the difference `b - a` is divisible by `c` and the quotient `(b - a) / c` is non-negative, the output 'YES' is printed. Otherwise, if either `b - a` is not divisible by `c` or `(b - a) / c` is negative, the output 'NO' is printed.
    #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers assigned from input values. If `c` equals 0 and `a` equals `b`, then 'YES' is printed, and `c` remains 0. If `c` equals 0 and `a` does not equal `b`, `c` is still 0. If `c` is not equal to 0, then if the difference `b - a` is divisible by `c` and the quotient `(b - a) / c` is non-negative, 'YES' is printed. Otherwise, if either `b - a` is not divisible by `c` or `(b - a) / c` is negative, 'NO' is printed.
#Overall this is what the function does:The function accepts three integers `a`, `b`, and `c` via user input. If `c` is 0 and `a` equals `b`, it prints 'YES'; otherwise, it prints 'NO'. If `c` is not 0, it checks if the difference `b - a` is divisible by `c` and non-negative; if both conditions are met, it prints 'YES', otherwise it prints 'NO'. The function does not return any values; it only prints output based on the conditions evaluated.

