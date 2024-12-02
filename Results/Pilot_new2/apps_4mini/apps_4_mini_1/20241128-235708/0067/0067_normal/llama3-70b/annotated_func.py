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
                #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that `0 <= x, y, z <= 100`. If `z` is equal to 0, the output printed is '0'. Otherwise, `z` is greater than 0, while `x` remains equal to `y`, and both `x` and `y` are within the specified bounds.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that `0 <= x, y, z <= 100`. If `x` is equal to `y`, then if `z` is equal to 0, the output printed is '0'; otherwise, `x` remains equal to `y` with `z` greater than 0. If `x` is not equal to `y`, then `x` is less than or equal to `y + z`, `x` is greater than or equal to `y`, and the output is a question mark.
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that `0 <= x, y, z <= 100` and `x` is less than or equal to `y + z`. If `x` is less than `y`, then the character `'-'` is printed to the output. If `x` is equal to `y`, the output is '0' if `z` equals 0; otherwise, `x` remains equal to `y` with `z` greater than 0. If `x` is not equal to `y`, then `x` is greater than or equal to `y`, and the output is a question mark.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that `0 <= x, y, z <= 100`. If `x` is greater than `y + z`, the output is '+'; otherwise, if `x` is less than `y`, the output is '-'; if `x` is equal to `y`, the output is '0' if `z` equals 0; otherwise, `x` remains equal to `y` with `z` greater than 0; if `x` is not equal to `y`, then `x` is greater than or equal to `y`, and the output is a question mark.
#Overall this is what the function does:The function accepts no parameters and reads three non-negative integers `x`, `y`, and `z` from input. It compares these integers and prints '+' if `x` is greater than `y + z`, '-' if `x` is less than `y`, '0' if `x` equals `y` and `z` equals 0, '?' if `x` equals `y` and `z` is greater than 0, or '?' if `x` is greater than or equal to `y` but not equal to `y`. The function does not have any return value.

