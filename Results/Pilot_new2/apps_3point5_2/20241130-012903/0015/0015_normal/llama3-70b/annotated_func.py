#State of the program right berfore the function call: a, b, and c are integers such that -10^9 <= a, b, c <= 10^9.**
def func():
    a, b, c = map(int, input().split())
    if (c == 0) :
        if (a == b) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9. If a is equal to b, then c remains 0. If a is not equal to b, the program prints 'NO' and the values of a, b, and c remain the same as before the execution of the program fragment.
    else :
        if ((b - a) % c == 0 and (b - a) / c >= 0) :
            print('YES')
        else :
            print('NO')
        #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9. c is not equal to 0. If ((b - a) % c == 0 and (b - a) / c >= 0), then the values of a, b, and c remain unchanged. Otherwise, the program prints 'NO'.
    #State of the program after the if-else block has been executed: *a, b, and c are integers such that -10^9 <= a, b, c <= 10^9. If c == 0 and a equals b, then c remains 0. If c == 0 and a is not equal to b, the program prints 'NO' and the values of a, b, and c remain the same as before. If c is not equal to 0 and ((b - a) % c == 0 and (b - a) / c >= 0), then a, b, and c remain unchanged. Otherwise, the program prints 'NO'.
#Overall this is what the function does:The function `func` reads three integer values `a`, `b`, and `c` from input. If `c` is 0, it checks if `a` is equal to `b` and prints 'YES' if true, 'NO' otherwise. If `c` is not 0, it verifies if `c` divides the difference between `b` and `a` evenly and if the result is non-negative, then it prints 'YES'. If either condition is not met, it prints 'NO'. The function does not explicitly return any value, it only prints the corresponding result based on the conditions.

