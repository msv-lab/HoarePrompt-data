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
                #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers from input(). After executing the if-else block, if `z` is 0, the output is '0'. Otherwise, if `z` is not 0, the output is '?' and the values of `x`, `y`, and `z` remain unchanged as per the precondition.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers from input(). If `x` equals `y` and `z` is 0, the output is '0'. Otherwise, the output is '?' and the values of `x`, `y`, and `z` remain unchanged as per the precondition.
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers from input(). If `x` is less than `y`, the condition holds as it is. If `x` equals `y` and `z` is 0, the output is '0'. Otherwise, the output is '?' and the values of `x`, `y`, and `z` remain unchanged as per the precondition.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers from input(). If `x` is greater than the sum of `y` and `z`, the condition holds as it is. If `x` is less than `y`, the condition remains unchanged. If `x` equals `y` and `z` is 0, the output is '0'. Otherwise, the output is '?' and the values of `x`, `y`, and `z` remain unchanged as per the precondition.
#Overall this is what the function does:The function takes three non-negative integers \(x\), \(y\), and \(z\) as input, each ranging from 0 to 100. It then evaluates these inputs according to specific conditions and prints one of four possible outputs: '+', '-', '0', or '?'. The function does not return a value but modifies the console output based on the conditions met. If \(x\) is greater than \(y + z\), it prints '+'. If \(x\) is less than \(y\), it prints '-'. If \(x\) equals \(y\) and \(z\) is 0, it prints '0'. In all other cases, it prints '?'. The values of \(x\), \(y\), and \(z\) remain unchanged after the function executes.

