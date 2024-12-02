#State of the program right berfore the function call: a, b, and c are integers such that -10^9 ≤ a, b, c ≤ 10^9**
def func():
    a, b, c = map(int, input().split())
    if (c == 0) :
        if (a == b) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers such that -10^9 ≤ a, b, c ≤ 10^9. The current value of `c` is equal to 0. If `a` is equal to `b`, the values of `a`, `b`, and `c` remain unchanged. Otherwise, if `a` is not equal to `b`, the code prints 'NO' and the values of `a`, `b`, and `c` remain unchanged.
    else :
        if ((b - a) % c == 0 and (b - a) / c >= 0) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers such that -10^9 ≤ a, b, c ≤ 10^9. The value of `c` is not equal to 0. If ((b - a) % c == 0 and (b - a) / c >= 0) is true, then 'YES' is printed. If the condition is false, 'NO' is printed.
    #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers such that -10^9 ≤ a, b, c ≤ 10^9. If c == 0, then if a == b, the values of a, b, and c remain unchanged. Otherwise, if a != b, the code prints 'NO' and the values of a, b, and c remain unchanged. If c != 0, and ((b - a) % c == 0 and (b - a) / c >= 0) is true, 'YES' is printed. If the condition is false, 'NO' is printed.
#Overall this is what the function does:The function `func` reads three integers `a`, `b`, and `c` from the input. If `c` is 0, it checks if `a` is equal to `b` and prints 'YES' if true, 'NO' otherwise. If `c` is not 0, it verifies if `b - a` is divisible by `c` and the division result is non-negative, then it prints 'YES', otherwise 'NO'. The function does not return any value.

