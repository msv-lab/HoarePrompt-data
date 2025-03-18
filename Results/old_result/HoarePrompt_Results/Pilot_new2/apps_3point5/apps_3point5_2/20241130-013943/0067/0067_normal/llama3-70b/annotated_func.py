#State of the program right berfore the function call: x, y, z are non-negative integers such that 0 <= x, y, z <= 100.**
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
                #State of the program after the if-else block has been executed: *x, y, z are non-negative integers such that 0 <= x, y, z <= 100. x, y, z are assigned the values obtained from input split into integers. x is less than or equal to y + z. x is greater than or equal to y. The current values of x, y, z satisfy the condition x == y. If z == 0, then x is equal to y and y is equal to x. If z is not equal to 0, then x, y, z remain unchanged.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *x, y, z are non-negative integers such that 0 <= x, y, z <= 100. The values of x, y, z satisfy the conditions x == y. If z == 0, then x is equal to y and y is equal to x. If z is not equal to 0, then x, y, z remain unchanged. If x is not equal to y, x, y, z remain unchanged.
        #State of the program after the if-else block has been executed: *x, y, z are non-negative integers such that 0 <= x, y, z <= 100. If x < y, then the current value of x is less than y. If x == y and z == 0, then x is equal to y and y is equal to x. If z is not equal to 0 and x == y, x, y, z remain unchanged. If x is not equal to y, x, y, z remain unchanged.
    #State of the program after the if-else block has been executed: *x, y, z are non-negative integers such that 0 <= x, y, z <= 100. If x > y + z, the program prints '+'. If x < y, then x is less than y. If x == y and z == 0, then x is equal to y and y is equal to x. If z is not equal to 0 and x == y, x, y, z remain unchanged. If x is not equal to y, x, y, z remain unchanged.
#Overall this is what the function does:The function `func` reads three non-negative integers `x`, `y`, `z` from the input. It then checks the relationship between `x`, `y`, and `z` and prints a specific character based on the conditions. If `x` is greater than `y + z`, it prints '+'. If `x` is less than `y`, it prints '-'. If `x` is equal to `y` and `z` is 0, it prints '0'. If `x` is equal to `y` and `z` is not 0, it prints '?'. If none of the above conditions are met, it also prints '?'. The function does not explicitly return any values or accept parameters.

