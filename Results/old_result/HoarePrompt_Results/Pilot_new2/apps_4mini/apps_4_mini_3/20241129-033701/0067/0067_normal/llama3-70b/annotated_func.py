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
                #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers such that 0 <= `x`, `y`, `z` <= 100, `x` is less than or equal to `y + z`, and `x` is greater than or equal to `y`. If `z` is equal to 0, then `x` is equal to `y` and `z` is 0. If `z` is greater than 0, then `x` is equal to `y` and `z` is greater than 0.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers such that 0 <= `x`, `y`, `z` <= 100, `x` is less than or equal to `y + z`, and `x` is greater than or equal to `y`. If `x` is equal to `y`, then if `z` is equal to 0, `x` is also 0; if `z` is greater than 0, `z` is greater than 0. If `x` is not equal to `y`, the output is '?'
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers such that 0 <= `x`, `y`, `z` <= 100, and `x` is less than or equal to `y + z`. If `x` is less than `y`, the function processes under this condition. If `x` is greater than or equal to `y`, then if `x` is equal to `y`, it checks the value of `z`: if `z` is equal to 0, then `x` is also 0; if `z` is greater than 0, `z` remains greater than 0. If `x` is not equal to `y`, the output is '?'
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers such that 0 <= `x`, `y`, `z` <= 100. If `x` is greater than the sum of `y` and `z`, the output is '+'. If `x` is less than or equal to `y + z`, and `x` is less than `y`, the output is processed under that condition. If `x` is greater than or equal to `y`, when `x` equals `y`, if `z` is equal to 0, then `x` is also 0; if `z` is greater than 0, then `z` remains greater than 0. If `x` is not equal to `y`, the output is '?'.
#Overall this is what the function does:The function accepts three integers `x`, `y`, and `z` via input, where each integer is in the range of 0 to 100. It compares `x` with `y` and `z` in various conditions: if `x` is greater than the sum of `y` and `z`, it prints '+'; if `x` is less than `y`, it prints '-'; if `x` is equal to `y`, it checks `z` and prints '0' if `z` is 0 or '?' if `z` is greater than 0; if `x` is not equal to `y` and is less than or equal to `y + z`, it prints '?'. The function does not return any values, only prints output based on these conditions.

