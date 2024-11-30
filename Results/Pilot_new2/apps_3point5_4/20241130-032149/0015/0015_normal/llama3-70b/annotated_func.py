#State of the program right berfore the function call: a, b, and c are integers such that -10^9 <= a, b, c <= 10^9.**
def func():
    a, b, c = map(int, input().split())
    if (c == 0) :
        if (a == b) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9. The current value of c is 0. If a is equal to b, then the current values of a and b are equal. If a is not equal to b, then the values of a and b are not equal to each other, and 'NO' has been printed.
    else :
        if ((b - a) % c == 0 and (b - a) / c >= 0) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9 and c is not equal to 0. If (b - a) % c == 0 and (b - a) / c >= 0, then 'YES' is printed. If the condition is not satisfied, then 'NO' is printed.
    #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9. If c == 0, then if a is equal to b, a and b retain their values. If a is not equal to b, a and b remain not equal, and 'NO' has been printed. If c is not equal to 0, then if (b - a) % c == 0 and (b - a) / c >= 0, 'YES' is printed. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function `func` reads three integers a, b, and c as input. If c is 0, it checks if a is equal to b and prints 'YES', otherwise it prints 'NO'. If c is not 0, it verifies if (b - a) is divisible by c and the result is non-negative, then it prints 'YES', otherwise it prints 'NO'. The function does not accept any parameters explicitly and operates solely based on user input.

