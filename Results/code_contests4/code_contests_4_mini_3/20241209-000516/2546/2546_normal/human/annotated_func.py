#State of the program right berfore the function call: A, B, and C are integers such that 1 ≤ A, B, C ≤ 10.
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
            #State of the program after the if-else block has been executed: *`a`, `b`, `c` are integers such that 1 ≤ `a`, `b`, `c` ≤ 10, and it is not the case that `a` is 5, `b` is 7, and `c` is 5. If `a` is 7, `b` is 5, and `c` is 5, then 'YES' is printed. Otherwise, 'NO' is printed.
        #State of the program after the if-else block has been executed: *`a`, `b`, `c` are integers such that 1 ≤ `a`, `b`, `c` ≤ 10, if `a` is 5, `b` is 7, and `c` is 5, then 'YES' is printed. If `a` is 7, `b` is 5, and `c` is 5, then 'YES' is printed. In all other cases, 'NO' is printed.
    #State of the program after the if-else block has been executed: *`a`, `b`, `c` are integers such that 1 ≤ `a`, `b`, `c` ≤ 10. If `a` is 5, `b` is 5, and `c` is 7, then 'YES' is printed. If `a` is 5, `b` is 7, and `c` is 5, or if `a` is 7, `b` is 5, and `c` is 5, then 'YES' is printed. In all other cases, 'NO' is printed.
#Overall this is what the function does:The function accepts no parameters and reads three integers from input, constrained by 1 ≤ a, b, c ≤ 10. It prints 'YES' if the integers are (5, 5, 7), (5, 7, 5), or (7, 5, 5), and 'NO' for any other combination of these integers. The function does not return any values.

