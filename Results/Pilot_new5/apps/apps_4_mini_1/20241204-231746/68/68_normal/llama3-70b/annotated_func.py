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
                #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers with values such that 0 <= `x`, `y`, `z` <= 100. If `z` is 0, the output '0' is printed. If `z` is greater than 0, then `x` is less than or equal to the sum of `y` and `z` (i.e., `x` <= `y + z`), `x` is greater than or equal to `y` (i.e., `x >= y`), and the current value of `x` is equal to `y` (i.e., `x == y`).
            else :
                print('?')
            #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers with values such that 0 <= `x`, `y`, `z` <= 100. If `x` is equal to `y`, then if `z` is 0, the output '0' is printed. If `z` is greater than 0, `x` equals `y`, and both conditions `x <= y + z` and `x >= y` hold true. Otherwise, if `x` is not equal to `y`, then `x` is less than or equal to the sum of `y` and `z`, `x` is greater than or equal to `y`, and the output is '?'.
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers such that 0 <= `x`, `y`, `z` <= 100 and `x` <= `y + z`. If `x` is less than `y`, the function continues with the current values of `x`, `y`, and `z`. If `x` is equal to `y`, the function prints '0' if `z` is 0; if `z` is greater than 0, it checks `x <= y + z` and `x >= y`. If `x` is not equal to `y`, the function outputs '?' given that `x` is greater than or equal to `y` and still satisfies `x <= y + z`.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers with values between 0 and 100. If `x` is greater than the sum of `y` and `z`, the output is '+'; otherwise, if `x` is less than `y`, the program continues with the current values of `x`, `y`, and `z`. If `x` equals `y`, the function prints '0' if `z` is 0, and if `z` is greater than 0, it checks `x <= y + z` and `x >= y`. If `x` is greater than or equal to `y` and `x` is not equal to `y`, the output is '?', indicating that `x` meets the conditions of being less than or equal to `y + z`.
#Overall this is what the function does:The function accepts three integer inputs x, y, and z (all between 0 and 100) and prints a character based on their values: it prints '+' if x is greater than the sum of y and z, '-' if x is less than y, '0' if x equals y and z is 0, '?' if x equals y and z is greater than 0, and '?' if x is greater than or equal to y but not equal to it. The function does not return any values.

