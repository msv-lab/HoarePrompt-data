#State of the program right berfore the function call: x, y, and z are non-negative integers such that 0 <= x,y,z <= 100.**
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
                #State of the program after the if-else block has been executed: *x, y, z are non-negative integers such that 0 <= x, y, z <= 100. x is not greater than y + z is true. x is not less than y, x is greater than or equal to y, x is not greater than y + z. x is equal to y. If z == 0, then z remains 0. If z != 0, then z is updated to a non-zero value.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *x, y, z are non-negative integers such that 0 <= x, y, z <= 100. x is not greater than y + z is true. x is not less than y, x is greater than or equal to y, x is not greater than y + z. If x == y, then in the if part, if z == 0, then z remains 0. If z != 0, then z is updated to a non-zero value. In the else part, where x is not equal to y, the program's state is not altered.
        #State of the program after the if-else block has been executed: *x, y, z are non-negative integers such that 0 <= x, y, z <= 100. The condition x is not greater than y + z is true. If x < y, then the program's state remains unchanged. If x == y, and z == 0, then z remains 0. If x == y, and z != 0, then z is updated to a non-zero value. If x is not less than y, x is greater than or equal to y, and x is not greater than y + z, the program's state remains unchanged.
    #State of the program after the if-else block has been executed: *x, y, z are non-negative integers such that 0 <= x, y, z <= 100. If x > y + z, then the program's state remains unchanged. If x is not greater than y + z, the following conditions apply: if x < y, the program's state remains unchanged. If x == y and z == 0, z remains 0. If x == y and z != 0, z is updated to a non-zero value. If x is not less than y, x is greater than or equal to y, and x is not greater than y + z, the program's state remains unchanged.
#Overall this is what the function does:The function `func` reads three non-negative integers x, y, and z from the input. It then performs a series of comparisons based on the values of x, y, and z and prints out different symbols ('+', '-', '0', or '?') based on the conditions met. The function does not explicitly return any value. The program works with predefined non-negative integers x, y, and z such that 0 <= x, y, z <= 100.

