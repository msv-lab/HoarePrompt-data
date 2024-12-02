#State of the program right berfore the function call: x, y, and z are integers such that 0 <= x, y, z <= 100.
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
                #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers such that 0 <= `x`, `y`, `z` <= 100, `x` is less than or equal to `y + z`, `x` is greater than or equal to `y`, and the current value of `x` is equal to the current value of `y`. If `z` is 0, the current values of `x` and `y` remain unchanged. If `z` is greater than 0, a string '?' is printed.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers such that 0 <= `x`, `y`, `z` <= 100, `x` is less than or equal to `y + z`, `x` is greater than or equal to `y`. If `x` is equal to `y`, if `z` is 0, then `x` and `y` remain unchanged, otherwise, a string '?' is printed. If `x` is not equal to `y`, a string '?' is printed.
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers such that 0 <= `x`, `y`, `z` <= 100 and `x` is less than or equal to `y + z`. If `x` is less than `y`, the function proceeds without a specific return value. If `x` is greater than or equal to `y`, and `x` is equal to `y`, then if `z` is 0, `x` and `y` remain unchanged; otherwise, a string '?' is printed. If `x` is not equal to `y`, a string '?' is printed.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers such that 0 <= `x`, `y`, `z` <= 100. If `x` is greater than `y + z`, the output is '+'. If `x` is less than or equal to `y + z`, and `x` is less than `y`, the function proceeds without a specific return value. If `x` is greater than or equal to `y`, and `x` is equal to `y`, then if `z` is 0, `x` and `y` remain unchanged; otherwise, a string '?' is printed. If `x` is not equal to `y`, a string '?' is printed.
#Overall this is what the function does:The function accepts three integers `x`, `y`, and `z` through input, which must be in the range of 0 to 100. It prints '+' if `x` is greater than `y + z`. If `x` is less than `y`, it does not output anything. If `x` is equal to `y`, it prints '0' if `z` is 0, or '?' if `z` is greater than 0. If `x` is greater than or equal to `y` and not equal to `y`, it simply prints '?'. There is no return value from the function.

