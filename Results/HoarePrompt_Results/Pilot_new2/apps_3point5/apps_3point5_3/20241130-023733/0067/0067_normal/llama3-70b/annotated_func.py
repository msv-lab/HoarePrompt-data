#State of the program right berfore the function call: x, y, z are integers such that 0 <= x, y, z <= 100.**
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
                #State of the program after the if-else block has been executed: *x, y, z are integers such that 0 <= x, y, z <= 100. x, y, z are assigned values parsed from input split by space. x is less than or equal to y + z. In the current state, x is equal to y. If z == 0, after executing the code, x is still equal to y and z is equal to 0. If z is not equal to 0, x is still equal to y but z remains unchanged.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *x, y, z are integers such that 0 <= x, y, z <= 100. x, y, z are assigned values parsed from input split by space. x is less than or equal to y + z. In the current state, if x == y, then after executing the code, if z == 0, x is still equal to y and z is equal to 0. If z is not equal to 0, x is still equal to y but z remains unchanged. If x is not equal to y, the values of x, y, and z remain unchanged.
        #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers such that 0 <= `x`, `y`, `z` <= 100. `x`, `y`, `z` are assigned values parsed from input. `x` is less than or equal to `y + z`. If `x` is less than `y`, the values of `x`, `y`, and `z` remain unchanged. If `x` is equal to `y`, after executing the code, if `z` is 0, `x` remains equal to `y` and `z` is set to 0. If `z` is not 0, `x` remains equal to `y` and `z` remains unchanged.
    #State of the program after the if-else block has been executed: *`x`, `y`, `z` are integers such that 0 <= `x`, `y`, `z` <= 100. If `x` is greater than `y + z`, the program prints '+'. If `x` is less than or equal to `y + z`, then:
    #- If `x` < `y`, `x`, `y`, and `z` remain unchanged.
    #- If `x` == `y` and `z` == 0, `x` is equal to `y` and `z` is set to 0.
    #- If `x` == `y` and `z` != 0, `x` is equal to `y` and `z` remains unchanged.
#Overall this is what the function does:The function `func` reads input integers x, y, and z, and based on their values, it determines the relationship between them. If x is greater than the sum of y and z, it prints '+'. If x is less than or equal to the sum of y and z, it further checks:
- If x is less than y, it prints '-'.
- If x is equal to y, it checks the value of z:
  - If z is 0, it prints '0'.
  - If z is not 0, it prints '?'.
The function does not explicitly return any value but performs print statements based on the conditions met.

