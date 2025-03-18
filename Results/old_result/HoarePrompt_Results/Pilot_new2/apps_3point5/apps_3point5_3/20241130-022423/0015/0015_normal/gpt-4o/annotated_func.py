#State of the program right berfore the function call: a, b, and c are integers such that -10^9 <= a, b, c <= 10^9.**
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
            #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9. a, b, and c are assigned the integer values obtained from splitting the input. b is not equal to a. c is not equal to 0. If the condition ((b - a) % c == 0 and (b - a) / c >= 0) is true, then the program executes the if block. Otherwise, the program executes the else block and 'NO' is printed.
        #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9. b is not equal to a. If c == 0, the program prints 'NO'. If c is not equal to 0 and ((b - a) % c == 0 and (b - a) / c >= 0) is true, the program executes the if block. Otherwise, the program executes the else block and 'NO' is printed.
    #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9. If b == a, 'YES' is printed. If b is not equal to a, then if c == 0, 'NO' is printed. If c is not equal to 0 and ((b - a) % c == 0 and (b - a) / c >= 0) is true, the program executes the if block. Otherwise, the program executes the else block and 'NO' is printed.
#Overall this is what the function does:The function `func` reads three integers `a`, `b`, and `c` from the input. It then checks if `b` is equal to `a`, in which case it prints 'YES'. If `b` is not equal to `a`, it further checks if `c` is equal to 0, printing 'NO' if true. If `c` is not 0, it verifies whether the condition ((b - a) % c == 0 and (b - a) / c >= 0) holds true. If the condition is met, it prints 'YES'; otherwise, it prints 'NO'. Therefore, the function essentially determines relationships between `a`, `b`, and `c` and outputs 'YES' or 'NO' accordingly.

