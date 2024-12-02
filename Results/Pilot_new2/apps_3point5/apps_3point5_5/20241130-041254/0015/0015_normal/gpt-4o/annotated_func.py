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
            #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9; a, b, and c are assigned the integer values obtained from splitting the input. The values of b and a are not equal. c is not equal to 0. If (b - a) is divisible by c and the result is non-negative, 'YES' is printed. Otherwise, 'NO' is printed.
        #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9; a, b, and c are assigned the integer values obtained from splitting the input. The values of b and a are not equal. If c == 0, the program prints 'NO'. If c != 0 and (b - a) is divisible by c and the result is non-negative, 'YES' is printed. Otherwise, 'NO' is printed.
    #State of the program after the if-else block has been executed: *a, b, and c are integers in the range -10^9 <= a, b, c <= 10^9. If b == a, 'YES' is printed. If b != a, and c == 0, 'NO' is printed. If b != a, c != 0, and (b - a) is divisible by c and the result is non-negative, 'YES' is printed. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function reads three integer inputs, a, b, and c, and checks if b equals a. If b is equal to a, it prints 'YES'. If b is not equal to a, it checks if c is equal to 0. If c is 0, it prints 'NO'. If c is not 0, it checks if (b - a) is divisible by c and the result is non-negative. If these conditions are met, it prints 'YES'; otherwise, it prints 'NO'.

