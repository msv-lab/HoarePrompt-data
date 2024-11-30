#State of the program right berfore the function call: a, b, and c are integers such that -10^9 <= a, b, c <= 10^9.**
def func():
    a, b, c = map(int, input().split())
    if (c == 0) :
        if (a == b) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9. The values of a, b, and c are assigned by the user input after splitting them by spaces. Initially, c is set to 0. If a equals b, then 'YES' is printed. If a does not equal b, then 'NO' is printed.
    else :
        if ((b - a) % c == 0 and (b - a) / c >= 0) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9. c is not equal to 0. If (b - a) % c == 0 and (b - a) / c >= 0, 'YES' is printed. If the condition is not met, 'NO' is printed.
    #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9. The values of a, b, and c are assigned by the user input after splitting them by spaces. Initially, if c == 0, then if a equals b, 'YES' is printed. If a does not equal b, 'NO' is printed. If c is not equal to 0, then if (b - a) % c == 0 and (b - a) / c >= 0, 'YES' is printed. If the condition is not met, 'NO' is printed.
#Overall this is what the function does:The function `func` reads three integer values `a`, `b`, and `c` from user input. If `c` is 0, it checks if `a` is equal to `b` and prints 'YES' if they are equal, 'NO' otherwise. If `c` is not 0, it checks if the difference between `b` and `a` is divisible by `c` and the division result is non-negative, then prints 'YES', otherwise 'NO'. The function does not accept any parameters and operates solely on user input.

