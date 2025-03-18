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
                #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100, `x` is less than or equal to `y + z`, `x` is greater than or equal to `y`, currently, `x` is equal to `y`. If `z` is 0, the output printed is '0'. If `z` is greater than 0, the output reflects the values of `x`, `y`, and `z`, adhering to the initial conditions.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100, `x` is less than or equal to `y + z`, and `x` is greater than or equal to `y`. If `x` is equal to `y`, if `z` is 0, the output printed is '0'. If `z` is greater than 0, the output reflects the values of `x`, `y`, and `z`. If `x` is not equal to `y`, the program continues without specifying output.
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100, and `x` is less than or equal to `y + z`. If `x` is less than `y`, the program proceeds without output. If `x` is equal to `y`, then if `z` is 0, the output printed is '0', otherwise the output reflects the values of `x`, `y`, and `z`. If `x` is greater than or equal to `y`, the program continues without specifying output.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100. If `x` is greater than `y + z`, the output is '+'. If `x` is less than or equal to `y + z`, and `x` is less than `y`, there is no output. If `x` is equal to `y`, then if `z` is 0, the output is '0'; otherwise, the output reflects the values of `x`, `y`, and `z`. If `x` is greater than or equal to `y`, the program continues without specifying output.
#Overall this is what the function does:The function accepts three non-negative integer parameters `x`, `y`, and `z`, with the constraints \(0 \leq x, y, z \leq 100\). It outputs a character based on the relationship between these values. If `x` is greater than the sum of `y` and `z`, it outputs '+'; if `x` is less than `y`, it produces no output; if `x` equals `y`, it evaluates `z`: if `z` is 0, output is '0', otherwise it outputs '?'. If `x` is greater than or equal to `y`, without checking the exact value of `z`, it outputs '?'. Finally, if `x` is less than or equal to `y + z`, but greater than or equal to `y`, the function does not generate any output. There are situations where there might be no output produced even if conditions are met, which may not have been explicitly captured in the annotations.

