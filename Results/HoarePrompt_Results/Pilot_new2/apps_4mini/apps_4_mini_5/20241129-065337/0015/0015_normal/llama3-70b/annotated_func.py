#State of the program right berfore the function call: a, b, and c are integers such that -10^9 ≤ a, b, c ≤ 10^9.
def func():
    a, b, c = map(int, input().split())
    if (c == 0) :
        if (a == b) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`a`, `b`, `c` are integers satisfying -10^9 ≤ `a`, `b`, `c` ≤ 10^9. If `a` is equal to `b`, then "YES" is printed. Otherwise, if `a` is not equal to `b`, "NO" is printed.
    else :
        if ((b - a) % c == 0 and (b - a) / c >= 0) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`a`, `b`, `c` are integers satisfying -10^9 ≤ `a`, `b`, `c` ≤ 10^9, and `c` is not equal to 0. If `(b - a)` is divisible by `c` and `(b - a) / c` is non-negative, the output is 'YES'. Otherwise, the output is 'NO'.
    #State of the program after the if-else block has been executed: *`a`, `b`, `c` are integers satisfying -10^9 ≤ `a`, `b`, `c` ≤ 10^9. If `c` is equal to 0 and `a` is equal to `b`, then "YES" is printed. If `c` is equal to 0 and `a` is not equal to `b`, "NO" is printed. If `c` is not equal to 0, then if `(b - a)` is divisible by `c` and `(b - a) / c` is non-negative, the output is 'YES'; otherwise, the output is 'NO'.
#Overall this is what the function does:The function accepts three integers `a`, `b`, and `c` via input. It checks if `c` is zero; if so, it prints 'YES' if `a` equals `b`, or 'NO' otherwise. If `c` is not zero, it checks if the difference `(b - a)` is divisible by `c` and whether the quotient `(b - a) / c` is non-negative, printing 'YES' if both conditions are met, or 'NO' if either condition fails. The function does not return any value.

