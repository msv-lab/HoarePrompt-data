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
            #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9. b is not equal to a. c is not equal to 0. If ((b - a) % c == 0 and (b - a) / c >= 0), 'YES' is printed. If either ((b - a) % c != 0) or ((b - a) / c < 0), 'NO' is printed.
        #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9. The variables a and b are assigned values based on the input split operation, and b is not equal to a. If c == 0, the program prints 'NO'. Otherwise, if ((b - a) % c == 0 and (b - a) / c >= 0), the program prints 'YES'. If either ((b - a) % c != 0) or ((b - a) / c < 0), the program prints 'NO'.
    #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9. If b equals a, then 'YES' is printed. Otherwise, if c == 0, 'NO' is printed. If ((b - a) % c == 0 and (b - a) / c >= 0), 'YES' is printed. If either ((b - a) % c != 0) or ((b - a) / c < 0), 'NO' is printed.
#Overall this is what the function does:The function reads three integers a, b, and c from input. It then checks if b is equal to a and prints 'YES'. If b is not equal to a, it checks if c is equal to 0 and prints 'NO'. If c is not 0, it verifies if the difference between b and a is divisible by c and the result of the division is non-negative. If both conditions are met, it prints 'YES'; otherwise, it prints 'NO'. The function handles cases where b equals a, c is 0, and the division result is negative.

