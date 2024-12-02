#State of the program right berfore the function call: # Precondition

**x, y, and z are non-negative integers such that 0 <= x,y,z <= 100.**
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
                #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100. The condition (x <= y + z) is true. `x` is greater than or equal to `y`. In the current state, `x` is equal to `y`. If z == 0, then after the execution, `z` is set to 0. If z is not equal to 0, then `x` is still equal to `y`, `x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100, `x` is greater than or equal to `y`, and z is not equal to 0.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100. The condition (x <= y + z) is true and `x` is greater than or equal to `y`. If `x` is equal to `y` and z == 0, then after the execution, `z` is set to 0. If z is not equal to 0, then `x` is still equal to `y`, `x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100, `x` is greater than or equal to `y`, and z is not equal to 0. If `x` is not equal to `y`, the relationship `x <= y` is maintained.
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100. `x`, `y`, and `z` are assigned the integer values obtained from splitting the input. The condition (x <= y + z) is true. If `x` is less than `y`, then `x` is less than `y` and the initial conditions are retained. If `x` is greater than or equal to `y`, several cases arise: if `x` is equal to `y` and z == 0, then after the execution, `z` is set to 0. If z is not equal to 0, then `x` is still equal to `y`, `x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100, `x` is greater than or equal to `y`, and z is not equal to 0. If `x` is not equal to `y`, the relationship `x <= y` is maintained.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are non-negative integers such that 0 <= `x`, `y`, `z` <= 100. The initial conditions are retained. In the case where x > y + z, the '+' symbol is printed without affecting the variable values. In the else part, if `x` is less than `y`, the relationship is maintained, and the initial conditions are retained. If `x` is equal to `y` and `z` == 0, then after execution, `z` is set to 0. If `x` is equal to `y` and `z` is not equal to 0, the conditions ensure that `x`, `y`, and `z` remain as non-negative integers such that 0 <= `x`, `y`, `z` <= 100, `x` is greater than or equal to `y`, and `z` is not equal to 0. If `x` is not equal to `y`, the relationship `x <= y` is maintained.
#Overall this is what the function does:The function `func` reads three non-negative integer values x, y, and z within the range 0 to 100. It then evaluates the relationship between x, y, and z based on certain conditions and prints symbols such as '+', '-', '0', or '?' accordingly. The function does not return any value.

