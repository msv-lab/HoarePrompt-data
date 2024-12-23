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
                #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= x, y, z <= 100, and both `x` and `y + z` satisfy the condition `x >= y`. If `z` equals 0, the string '0' is printed. Otherwise, a question mark is printed.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= x, y, z <= 100, and both `x` and `y + z` satisfy the condition `x >= y`. If `x == y` and `z == 0`, then the string '0' is printed. If `x == y` and `z != 0`, then a question mark is printed. If `x > y`, then no specific action is performed other than maintaining the conditions `0 <= x, y, z <= 100` and `x > y`.
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= x, y, z <= 100. Both `x` and `y + z` satisfy the condition `x <= y + z`. If `x < y`, the output of the program is `-`. Otherwise, if `x == y` and `z == 0`, the string '0' is printed. If `x == y` and `z != 0`, a question mark is printed. If `x > y`, no specific action is performed other than maintaining the conditions `0 <= x, y, z <= 100` and `x >= y`.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100. If `x` > `y` + `z`, the output is '+'. Otherwise, if `x` < `y`, the output is '-'. If `x` == `y` and `z` == 0, the output is '0'. If `x` == `y` and `z` != 0, the output is '?'. In all other cases, the values of `x`, `y`, and `z` remain within the specified range without any specific change, and no output is produced.
#Overall this is what the function does:The function accepts no parameters and reads three non-negative integers \(x\), \(y\), and \(z\) from the user, each within the range of 0 to 100. It then evaluates these integers and prints one of four possible outputs: '+', '-', '0', or '?'. Specifically:
- If \(x > y + z\), it prints '+'.
- If \(x < y\), it prints '-'.
- If \(x == y\) and \(z == 0\), it prints '0'.
- If \(x == y\) and \(z != 0\), it prints '?'.
- In all other cases, no specific output is produced, but the conditions \(0 \leq x, y, z \leq 100\) and \(x \geq y\) or \(x \leq y + z\) are maintained.

