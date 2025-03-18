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
            #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers assigned from input values, with `b` not equal to `a` and `c` not equal to 0. If the difference between `b` and `a` is divisible by `c` and the result of the division `(b - a) / c` is greater than or equal to 0, then "YES" is printed. Otherwise, if the difference is not divisible by `c` or the result of the division is less than 0, "YES" is not printed.
        #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers assigned from input values, with `b` not equal to `a`. If `c` is 0, the function does not perform any further operation. Otherwise, if `c` is not 0 and the difference between `b` and `a` is divisible by `c` and the result of the division `(b - a) / c` is greater than or equal to 0, then "YES" is printed. If the conditions for printing "YES" are not met, nothing is printed.
    #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers. If `b` is equal to `a`, then 'YES' is printed. If `b` is not equal to `a`, and if `c` is 0, no further operations are performed. Otherwise, if `c` is not 0 and `(b - a)` is divisible by `c` with the quotient being greater than or equal to 0, then 'YES' is printed. If these conditions are not met, nothing is printed.
#Overall this is what the function does:The function accepts three integers `a`, `b`, and `c` from user input. It prints 'YES' if `b` is equal to `a`. If `b` is not equal to `a` and `c` is 0, it prints 'NO'. If `c` is not 0, it checks if the difference `(b - a)` is divisible by `c` and the result of the division `(b - a) / c` is non-negative; it prints 'YES' if both conditions are met, otherwise it prints 'NO'. If none of the conditions are met for printing, nothing is printed.

