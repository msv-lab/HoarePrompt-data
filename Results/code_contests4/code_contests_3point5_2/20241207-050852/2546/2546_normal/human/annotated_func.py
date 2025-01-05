#State of the program right berfore the function call: A, B, and C are integers such that 1 <= A, B, C <= 10.**
def func():
    a, b, c = map(int, raw_input().split())
    if (a == 5 and b == 5 and c == 7) :
        print('YES')
    else :
        if (a == 5 and b == 7 and c == 5) :
            print('YES')
        else :
            if (a == 7 and b == 5 and c == 5) :
                print('YES')
            else :
                print('NO')
            #State of the program after the if-else block has been executed: *A, B, C are integers such that 1 <= A, B, C <= 10. a, b, and c are not all equal to 5, or c is not equal to 7 in case a and b are 5, and (a is not equal to 5 or b is not equal to 7 or c is not equal to 5). If a == 7 and b == 5 and c == 5, the function returns 'YES'. Otherwise, the function returns 'NO'.
        #State of the program after the if-else block has been executed: *A, B, and C are integers such that 1 <= A, B, C <= 10. a, b, and c are not all equal to 5, or c is not equal to 7 if a and b are 5. If a == 5 and b == 7 and c == 5, 'YES' is printed. If a == 7 and b == 5 and c == 5, the function returns 'YES'. Otherwise, the function returns 'NO'.
    #State of the program after the if-else block has been executed: *A, B, and C are integers such that 1 <= A, B, C <= 10. If A == 5, B == 5, and C == 7, 'YES' is printed as output. If A and B are 5 but C is not 7, or A and B are not 5 but C is 7, 'YES' is printed. If A is 5 and B is 7 and C is 5, 'YES' is printed. If A is 7 and B is 5 and C is 5, 'YES' is printed. Otherwise, 'NO' is printed.
#Overall this is what the function does:The function `func` reads three integers A, B, and C from the user input. It then checks the values of A, B, and C to determine if they match specific conditions. If A = 5, B = 5, and C = 7, or A = 5, B = 7, and C = 5, or A = 7, B = 5, and C = 5, it prints 'YES'. Otherwise, it prints 'NO'. The function does not explicitly return any value. Edge cases and missing functionality include situations where the input values do not match any of the specified conditions.

