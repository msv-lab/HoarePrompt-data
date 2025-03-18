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
            #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9. b is not equal to a. c is not equal to 0. If ((b - a) % c == 0 and (b - a) / c >= 0) is true, 'YES' is printed. If the condition is false, 'NO' is printed.
        #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9. b is not equal to a. If c == 0, 'NO' is printed. Otherwise, if ((b - a) % c == 0 and (b - a) / c >= 0) is true, 'YES' is printed. If the condition is false, 'NO' is printed.
    #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers such that -10^9 <= a, b, c <= 10^9. `a`, `b`, and `c` are assigned the values obtained from splitting the input string into integers. If `b` is equal to `a`, 'YES' is printed. If `b` is not equal to `a`, then if `c` is 0, 'NO' is printed. Otherwise, if ((b - a) % c == 0 and (b - a) / c >= 0) is true, 'YES' is printed. If the condition is false, 'NO' is printed.
#Overall this is what the function does:The function takes three integer inputs a, b, and c. It then checks if b is equal to a and prints 'YES'. If b is not equal to a, it further checks if c is 0, printing 'NO' in that case. If c is not 0, it verifies whether (b - a) is divisible by c and the division result is non-negative. If both conditions are met, it prints 'YES'; otherwise, it prints 'NO'.

