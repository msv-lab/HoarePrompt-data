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
            #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers between 1 and 10. The values of `a` and `b` are not equal to 5, or the value of `c` is not equal to 7. The values of `a` and `b` are not both 5 and 7, or `c` is not equal to 5. The values of `a` and `b` are not 7 and 5, or `c` is not 5. If `a` is 7, `b` is 5, and `c` is 5, then 'YES' is printed. Otherwise, the original conditions are maintained.
        #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers between 1 and 10. The values of `a` and `b` are not equal to 5, or the value of `c` is not equal to 7. The values of `a` and `b` are not both 5 and 7, or `c` is not equal to 5. The values of `a` and `b` are not 7 and 5, or `c` is not 5. If `a` is 5, `b` is 7, and `c` is 5, then 'YES' is printed. If `a` is 7, `b` is 5, and `c` is 5, then 'YES' is printed. Otherwise, the original conditions are maintained.
    #State of the program after the if-else block has been executed: *`a`, `b`, and `c` are integers between 1 and 10. If `a` is equal to 5, `b` is equal to 5, and `c` is equal to 7, then the program prints 'YES'. Otherwise, the program maintains the original conditions stated in the precondition.
#Overall this is what the function does:The function `func` takes input from the user for three integers a, b, and c. It then checks if a, b, and c match specific values (5, 5, 7), (5, 7, 5), or (7, 5, 5) in any order and prints 'YES' if any of these conditions are met. If none of the conditions are satisfied, it prints 'NO'. The function does not accept any parameters and operates solely based on the user input within the given constraints.

