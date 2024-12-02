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
            #State of the program after the if-else block has been executed: *`a`, `b`, `c` are integers, `b` is not equal to `a`, and `c` is not equal to 0. If `(b - a) % c == 0` and `(b - a) / c >= 0`, then 'YES' is printed. Otherwise, if either `(b - a) % c != 0` or `(b - a) / c < 0`, then 'NO' is printed.
        #State of the program after the if-else block has been executed: *`a`, `b`, `c` are integers, `b` is not equal to `a`. If `c` is 0, the function has no further operations related to `b` and `a`. If `c` is not 0, then if `(b - a) % c == 0` and `(b - a) / c >= 0`, 'YES' is printed; otherwise, 'NO' is printed.
    #State of the program after the if-else block has been executed: *`a`, `b`, `c` are integers. If `b` is equal to `a`, 'YES' is printed. If `b` is not equal to `a`, and `c` is 0, there are no further operations related to `b` and `a`. If `c` is not 0, then 'YES' is printed if `(b - a) % c == 0` and `(b - a) / c >= 0`; otherwise, 'NO' is printed.
#Overall this is what the function does:The function accepts three integers `a`, `b`, and `c` which are read from user input. It checks if `b` is equal to `a`, in which case it prints 'YES'. If `b` is not equal to `a`, it further checks if `c` is zero, in which case it prints 'NO'. If `c` is not zero, it checks if the difference `(b - a)` is divisible by `c` and if the result of `(b - a) / c` is non-negative. It prints 'YES' if both conditions are met, otherwise it prints 'NO'. Therefore, the function can output 'YES' or 'NO' based on the values of `a`, `b`, and `c`, but does not return a value; it simply prints the result.

