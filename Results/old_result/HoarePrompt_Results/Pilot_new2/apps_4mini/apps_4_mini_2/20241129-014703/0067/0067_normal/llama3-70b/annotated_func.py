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
                #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers within the range [0, 100]. If `z` is 0, then '0' has been printed, and `x` is equal to `y`. Otherwise, `x` is less than or equal to `y + z`, `x` is greater than or equal to `y`, `x` is equal to `y`, and `z` is greater than 0.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers within the range [0, 100]. If `x` is equal to `y`, then if `z` is 0, '0' has been printed, and `x` is equal to `y`. If `z` is greater than 0, `x` is less than or equal to `y + z`, `x` is greater than or equal to `y`, `x` is equal to `y`, and `z` is greater than 0. Otherwise, if `x` is not equal to `y`, then `x` is still within the range [0, 100], `x` is less than or equal to `y + z`, `x` is greater than or equal to `y`, and `x` is not equal to `y.
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers within the range [0, 100]. If `x` is less than `y`, then `x` remains less than `y`. If `x` is equal to `y`, and if `z` is 0, '0' has been printed, and `x` is equal to `y`. If `z` is greater than 0, then `x` is less than or equal to `y + z`, `x` is equal to `y`, and `z` is greater than 0. If `x` is not equal to `y`, then `x` is still within the range [0, 100], `x` is less than or equal to `y + z`, `x` is greater than or equal to `y`, and `x` is not equal to `y.`
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers within the range [0, 100]. If `x` is greater than the sum of `y` and `z`, a '+' symbol is printed. If `x` is less than `y`, then `x` remains less than `y`. If `x` is equal to `y` and `z` is 0, '0' is printed, and `x` is equal to `y`. If `z` is greater than 0, then `x` is less than or equal to `y + z`, `x` is equal to `y`, and `z` is greater than 0. If `x` is not equal to `y`, then `x` remains within the range [0, 100], is less than or equal to `y + z`, is greater than or equal to `y`, and `x` is not equal to `y.`
#Overall this is what the function does:The function reads three integers `x`, `y`, and `z`, all constrained between 0 and 100. It prints a '+' if `x` is greater than the sum of `y` and `z`, a '-' if `x` is less than `y`, '0' if `x` equals `y` and `z` is 0, a '?' if `x` equals `y` and `z` is greater than 0, or a '?' if `x` is greater than or equal to `y` but not equal to `y`. The function does not return any values; it only prints the result.

