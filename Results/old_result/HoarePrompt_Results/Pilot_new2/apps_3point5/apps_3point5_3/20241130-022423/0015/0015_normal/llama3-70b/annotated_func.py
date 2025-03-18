#State of the program right berfore the function call: a, b, and c are integers such that -10^9 ≤ a, b, c ≤ 10^9.**
def func():
    a, b, c = map(int, input().split())
    if (c == 0) :
        if (a == b) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *a, b, c are integers such that -10^9 ≤ a, b, c ≤ 10^9. The current value of c is 0. If a is equal to b, 'YES' is printed. If a is not equal to b, the values of a and b are not changed and 'YES' is printed.
    else :
        if ((b - a) % c == 0 and (b - a) / c >= 0) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *a, b, c are integers such that -10^9 ≤ a, b, c ≤ 10^9. c is not equal to 0. If ((b - a) % c == 0 and (b - a) / c >= 0), 'YES' is printed. If the condition is not satisfied, 'NO' is printed.
    #State of the program after the if-else block has been executed: *a, b, c are integers such that -10^9 ≤ a, b, c ≤ 10^9. If c == 0 and a is equal to b, then 'YES' is printed. If c == 0 and a is not equal to b, a and b remain unchanged and 'YES' is printed. If c is not equal to 0 and ((b - a) % c == 0 and (b - a) / c >= 0), then 'YES' is printed. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function `func` reads three integers a, b, and c from input, and based on the values of a, b, and c, it determines whether to print 'YES' or 'NO' following specific conditions. If c is 0, it checks if a is equal to b and prints 'YES' accordingly. If c is not 0, it checks if (b - a) is divisible by c and the division result is non-negative to print 'YES'. If none of these conditions are met, it prints 'NO'. Therefore, the functionality of the function is to perform comparisons and print 'YES' or 'NO' based on the calculated conditions.

