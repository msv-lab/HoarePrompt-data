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
                #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers such that 0 <= `x`, `y`, `z` <= 100, and `x` is equal to `y`. If `z` is 0, then `x` remains equal to `y`, and `z` is 0. Otherwise, `z` is greater than 0 while `x` and `y` remain equal.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers such that 0 <= `x`, `y`, `z` <= 100. If `x` is equal to `y`, then if `z` is 0, `x` remains equal to `y` and `z` is 0; otherwise, `z` is greater than 0 while `x` and `y` remain equal. If `x` is not equal to `y`, then `x` satisfies the conditions that it is less than or equal to `y + z`, is greater than or equal to `y`, and is not equal to `y`.
        #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers input by the user such that 0 <= `x`, `y`, `z` <= 100 and `x` is less than or equal to `y + z`. If `x` is less than `y`, then the value of `x` remains unchanged. If `x` is equal to `y`, then if `z` is 0, `x` remains equal to `y` and `z` is 0; otherwise, `z` is greater than 0 while `x` and `y` remain equal. If `x` is not equal to `y`, then `x` satisfies the conditions that it is less than or equal to `y + z`, is greater than or equal to `y`, and is not equal to `y`.
    #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers input by the user such that 0 <= `x`, `y`, `z` <= 100. If `x` is greater than `y + z`, then `x` is confirmed to be greater than the sum of `y` and `z`. Otherwise, if `x` is less than or equal to `y + z`, and `x` is less than `y`, the value of `x` remains unchanged. If `x` is equal to `y`, then if `z` is 0, `x` remains equal to `y` and `z` is 0; otherwise, `z` is greater than 0 while both `x` and `y` remain equal. If `x` is not equal to `y`, then `x` satisfies the conditions of being less than or equal to `y + z`, greater than or equal to `y`, and not equal to `y`.
#Overall this is what the function does:The function accepts three integers `x`, `y`, and `z` (each between 0 and 100) as input and performs the following checks: If `x` is greater than the sum of `y` and `z`, it prints '+'; if `x` is less than `y`, it prints '-'; if `x` is equal to `y`, it further checks if `z` is 0, printing '0' for that case; if `z` is not 0, it prints '?'. For cases where `x` is not greater than `y + z`, not less than `y`, and not equal to `y`, it defaults to printing '?' regardless of the values of `y` and `z`. The function does not have a return statement, so it does not return any value, only prints outputs based on the conditions evaluated.

