#State of the program right berfore the function call: a, b, and c are integers such that -10^9 ≤ a, b, c ≤ 10^9.
def func():
    a, b, c = map(int, input().split())
    if (c == 0) :
        if (a == b) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers within the range -10^9 ≤ a, b, c ≤ 10^9. If `a` is equal to `b`, the output is 'YES'. Otherwise, `c` remains 0 and `a` is not equal to `b`.
    else :
        if ((b - a) % c == 0 and (b - a) / c >= 0) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are input integers within the range -10^9 ≤ a, b, c ≤ 10^9, and `c` is not equal to 0. If the difference (b - a) is divisible by c and (b - a) / c is greater than or equal to 0, 'YES' has been printed. Otherwise, if the difference (b - a) is not divisible by c or (b - a) / c is negative, 'NO' has been printed.
    #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers within the range -10^9 ≤ a, b, c ≤ 10^9. If `c` is equal to 0 and `a` is equal to `b`, the output is 'YES'. If `c` is equal to 0 and `a` is not equal to `b`, `c` remains 0 and `a` is not equal to `b`. If `c` is not equal to 0, then if the difference (b - a) is divisible by c and (b - a) / c is greater than or equal to 0, 'YES' is printed. Otherwise, if (b - a) is not divisible by c or (b - a) / c is negative, 'NO' is printed.
#Overall this is what the function does:The function accepts three integers `a`, `b`, and `c` through user input and performs the following checks: If `c` is equal to 0 and `a` is equal to `b`, it outputs 'YES'. If `c` is equal to 0 and `a` is not equal to `b`, it outputs 'NO'. If `c` is not equal to 0, it checks if the difference `(b - a)` is divisible by `c` and if the result of `(b - a) / c` is non-negative; if both conditions are met, it outputs 'YES', otherwise it outputs 'NO'. The function does not return any value.

