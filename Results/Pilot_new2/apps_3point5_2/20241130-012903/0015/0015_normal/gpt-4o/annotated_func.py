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
            #State of the program after the if-else block has been executed: *a, b, c are integers such that -10^9 <= a, b, c <= 10^9. b is not equal to a. c is not equal to 0. If (b - a) % c == 0 and (b - a) / c >= 0, 'YES' is printed. If either (b - a) % c != 0 or (b - a) / c < 0, 'NO' is printed.
        #State of the program after the if-else block has been executed: *a, b, c are integers such that -10^9 <= a, b, c <= 10^9. b is not equal to a. If c == 0, 'NO' is printed. If c is not equal to 0, if (b - a) % c == 0 and (b - a) / c >= 0, 'YES' is printed. If either (b - a) % c != 0 or (b - a) / c < 0, 'NO' is printed.
    #State of the program after the if-else block has been executed: *a, b, c are integers such that -10^9 <= a, b, c <= 10^9. If b == a, 'YES' is printed. If b is not equal to a, if c == 0, 'NO' is printed. If c is not equal to 0, if (b - a) % c == 0 and (b - a) / c >= 0, 'YES' is printed. If either (b - a) % c != 0 or (b - a) / c < 0, 'NO' is printed.
#Overall this is what the function does:The function takes three integers a, b, and c as input. It compares b and a, if they are equal, it prints 'YES'. If b and a are not equal, it checks if c is 0, in which case it prints 'NO'. If c is not 0, it verifies if (b - a) is divisible by c and the result is non-negative, then it prints 'YES'; otherwise, it prints 'NO'.

