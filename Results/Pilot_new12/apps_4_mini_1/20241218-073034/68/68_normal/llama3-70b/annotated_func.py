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
                #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers such that 0 <= `x`, `y`, `z` <= 100. If `z` is equal to 0, then `x`, `y`, and `z` are such that `x = y` and `z = 0`. If `z` is greater than 0, then `x`, `y`, `z` remain integers that satisfy the conditions 0 <= `x`, `y`, `z` <= 100, `x <= y + z`, `x >= y`, and the current value of `x` equals `y`.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers assigned values from user input such that 0 <= `x`, `y`, `z` <= 100. If `x` equals `y`, then if `z` equals 0, `x`, `y`, and `z` satisfy `x = y` and `z = 0`. If `z` is greater than 0, `x`, `y`, and `z` remain integers satisfying 0 <= `x`, `y`, `z` <= 100, `x <= y + z`, `x >= y`, and `x = y`. Otherwise, if `x` is not equal to `y`, `x`, `y`, and `z` are still integers satisfying the conditions and the output is '?'.
        #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers such that 0 <= `x`, `y`, `z` <= 100 and `x` is less than or equal to `y + z`. If `x` is less than `y`, the output is `'-'`. If `x` equals `y`, then either `z` equals 0 (yielding `x = y` and `z = 0`), or if `z` is greater than 0, the conditions are maintained with `x = y`, `x <= y + z`, and all integers remain valid. If `x` is not equal to `y`, the output is '?' while still satisfying the initial conditions.
    #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers such that 0 <= `x`, `y`, `z` <= 100. If `x` is greater than `y + z`, the output is '+'. If `x` is less than or equal to `y + z`, then if `x` is less than `y`, the output is '-'. If `x` equals `y`, the output depends on the value of `z`: either `z` equals 0 (yielding `x = y` and `z = 0`), or `z` is greater than 0, maintaining `x = y` and satisfying the other conditions. If `x` is not equal to `y`, the output is '?'.
#Overall this is what the function does:The function reads three integers `x`, `y`, and `z` from user input, each constrained between 0 and 100. It evaluates the relationship between these integers and produces different outputs based on certain conditions: if `x` is greater than `y + z`, it outputs '+'. If `x` is less than `y`, it outputs '-'. If `x` equals `y`, it further checks the value of `z`: if `z` is 0, it outputs '0', while if `z` is greater than 0, it outputs '?'. If `x` is not equal to either `y` or `y + z`, the output will also be '?'. Therefore, the function effectively categorizes the relationship between `x`, `y`, and `z` and returns an appropriate string without returning any values. Additionally, the function lacks handling for cases where the input values are out of the specified bounds (0 to 100).

