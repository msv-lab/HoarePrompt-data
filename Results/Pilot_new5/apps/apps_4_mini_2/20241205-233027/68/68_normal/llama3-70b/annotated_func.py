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
                #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers such that 0 <= `x`, `y`, `z` <= 100, `x` is less than or equal to `y + z`, and `x` is greater than or equal to `y`. If `z` is 0, the output is '0'. If `z` is greater than 0, the output is '?'.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers such that 0 <= `x`, `y`, `z` <= 100, `x` is less than or equal to `y + z`, and `x` is greater than or equal to `y`. If `x` is equal to `y`, the output is '0' if `z` is 0, otherwise, the output is '?'. If `x` is not equal to `y`, the output is '?'.
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers such that 0 <= `x`, `y`, `z` <= 100, and `x` is less than or equal to `y + z`. If `x` is less than `y`, then `'-'` is printed. If `x` is greater than or equal to `y`, and if `x` is equal to `y`, the output is '0' if `z` is 0, otherwise, the output is '?'. If `x` is not equal to `y`, the output is '?'.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers such that 0 <= `x`, `y`, `z` <= 100. If `x` is greater than `y + z`, the output is '+'. Otherwise, if `x` is less than `y`, the output is '-'. If `x` is greater than or equal to `y`, and if `x` equals `y`, the output is '0' if `z` is 0; otherwise, the output is '?'. If `x` is not equal to `y`, the output is '?'.
#Overall this is what the function does:The function accepts no parameters and reads three integers x, y, and z from input, constrained between 0 and 100. It prints '+' if x is greater than the sum of y and z; '-' if x is less than y; '0' if x equals y and z is 0; '?' if x equals y and z is greater than 0, or if x is greater than or equal to y but not equal to y. If x is not greater than y + z and does not fall into these specific cases, it defaults to printing '?'.

