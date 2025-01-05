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
            #State of the program after the if-else block has been executed: *`A`, `B`, and `C` are integers such that 1 <= A, B, C <= 10. If `a` is equal to 7, `b` is equal to 5, and `c` is equal to 5, then 'YES' is printed. Otherwise, if `a` is not 7, `b` is not 5, or `c` is not 5, then 'NO' is printed.
        #State of the program after the if-else block has been executed: *`A`, `B`, and `C` are integers such that 1 <= A, B, C <= 10. If `a` is 5, `b` is 7, and `c` is 5, then 'YES' is printed. Otherwise, if `a` is equal to 7, `b` is equal to 5, and `c` is equal to 5, then 'YES' is printed. In all other cases, 'NO' is printed.
    #State of the program after the if-else block has been executed: *`A`, `B`, and `C` are integers such that 1 <= A, B, C <= 10. If `a` is 5, `b` is 5, and `c` is 7, then 'YES' is printed. Otherwise, if `a` is 5, `b` is 7, and `c` is 5, or if `a` is 7, `b` is 5, and `c` is 5, then 'YES' is printed. In all other cases, 'NO' is printed.
#Overall this is what the function does:The function accepts input for three integers `a`, `b`, and `c` (from user input) and checks specific combinations of these values. It prints 'YES' if any of the following conditions are met: (5, 5, 7), (5, 7, 5), or (7, 5, 5). If none of these conditions are met, it prints 'NO'. The function does not return any value and does not handle cases outside of the specified combinations, meaning any inputs that don't match the conditions will simply result in 'NO'.

