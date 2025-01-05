#State of the program right berfore the function call: A, B, and C are integers such that 1 <= A, B, C <= 10.
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
            #State of the program after the if-else block has been executed: *A, B, and C are integers ranging from 1 to 10. If A is not equal to 5 or B is not equal to 7 or C is not equal to 5, the program does not enter the if block. If A is not equal to 5 or B is not equal to 5 or C is not equal to 7 and A is not equal to 7, B is equal to 5, and C is equal to 5, then 'YES' is printed. Otherwise, 'NO' is printed.
        #State of the program after the if-else block has been executed: A, B, and C are integers ranging from 1 to 10. If A is equal to 5, B is equal to 7, and C is equal to 5, then 'YES' is printed. If A is not equal to 5 or B is not equal to 7 or C is not equal to 5, the program does not enter the if block. If A is not equal to 5 or B is not equal to 5 or C is not equal to 7 and A is not equal to 7, B is equal to 5, and C is equal to 5, then 'YES' is printed. Otherwise, 'NO' is printed.
    #State of the program after the if-else block has been executed: *A, B, and C are integers ranging from 1 to 10. If a == 5, b == 5, and c == 7, then 'YES' is printed. If a == 5, b == 7, and c == 5, then 'YES' is printed. If none of these conditions are met, 'NO' is printed.
#Overall this is what the function does:The function `func` reads three integers A, B, and C as input and checks if they match specific values. If A is 5, B is 5, and C is 7, or A is 5, B is 7, and C is 5, or A is 7, B is 5, and C is 5, then 'YES' is printed; otherwise, 'NO' is printed. The function does not have any explicit return value specified.

