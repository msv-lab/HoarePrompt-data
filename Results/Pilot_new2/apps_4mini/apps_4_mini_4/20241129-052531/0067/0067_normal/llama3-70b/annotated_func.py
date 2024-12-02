#State of the program right berfore the function call: x, y, and z are non-negative integers such that 0 <= x, y, z <= 100.
def func():
    x, y, z = map(int, input().split())
    if (x > y + z) :
        print('+')
    else :
        if (x < y) :
            print('-')
        else :
            if (x == y) :
                if (z == 0) :
                    print('0')
                else :
                    print('?')
                #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100, `x` is less than or equal to `y + z`, and `x` is greater than or equal to `y`. If `z` is 0, '0' has been printed. Otherwise, `z` is greater than 0 and a question mark '?' is printed.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100; `x` is less than or equal to `y + z`; and `x` is greater than or equal to `y`. If `x` is equal to `y`, then if `z` is 0, '0' has been printed; otherwise, a question mark '?' is printed. If `x` is not equal to `y`, the program does not print anything specific.
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100; `x` is less than or equal to `y + z`. If `x` is less than `y`, the program execution will proceed without any specific output. If `x` is greater than or equal to `y`, and if `x` equals `y`, then if `z` is 0, '0' is printed; otherwise, a question mark '?' is printed. If `x` is not equal to `y`, the program does not print anything specific.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100. If `x` is greater than `y + z`, the output is '+'; otherwise, if `x` is less than `y`, there is no specific output. If `x` is greater than or equal to `y`, and if `x` equals `y`, then if `z` is 0, '0' is printed; otherwise, a question mark '?' is printed. If `x` is not equal to `y`, the program does not print anything specific.
#Overall this is what the function does:The function accepts three non-negative integers `x`, `y`, and `z`, which are read from input. It prints '+' if `x` is greater than the sum of `y` and `z`. If `x` is less than `y`, it does not print anything. If `x` is equal to `y`, it prints '0' if `z` is 0; otherwise, it prints '?'. If `x` is greater than `y` but not equal to it, it prints '?'. The function has no return value and should handle the case where `x`, `y`, and `z` are non-negative integers within the specified range.

