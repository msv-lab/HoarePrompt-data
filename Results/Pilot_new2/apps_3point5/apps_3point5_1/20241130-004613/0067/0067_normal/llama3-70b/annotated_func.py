#State of the program right berfore the function call: # Precondition

**x, y, and z are non-negative integers such that 0 <= x, y, z <= 100.**
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
                #State of the program after the if-else block has been executed: *x, y, and z are non-negative integers such that 0 <= x, y, z <= 100. x is less than or equal to y + z. x is greater than or equal to y. x is equal to y. If z == 0, then z remains 0 after the execution. If z is not equal to 0, then the value of z changes, but the rest of the conditions remain the same.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *x, y, and z are non-negative integers such that 0 <= x, y, z <= 100. x is less than or equal to y + z. x is greater than or equal to y. If x equals y, then depending on the value of z, the program will either keep z the same if z is 0 or update the value of z if z is not 0. If x is not equal to y, then the values of x, y, and z remain unchanged.
        #State of the program after the if-else block has been executed: *x, y, and z are non-negative integers such that 0 <= x, y, z <= 100. x is less than or equal to y + z. If x is less than y, then x remains unchanged. If x equals y and z is 0, then z remains unchanged. If x equals y and z is not 0, then z is updated. If x is not equal to y, then x, y, and z remain unchanged.
    #State of the program after the if-else block has been executed: *x, y, and z are non-negative integers such that 0 <= x, y, z <= 100. If x is greater than y + z, then x, y, and z remain unchanged. If x is less than or equal to y + z, then based on specific conditions, the values of x, y, and z may remain unchanged or be updated accordingly.
#Overall this is what the function does:The function reads input as three non-negative integers x, y, and z within the range of 0 to 100. It then compares these values and prints specific symbols based on the conditions. If x is greater than y + z, it prints '+'. If x is less than y, it prints '-'. If x equals y, it further checks if z is 0 and prints '0' in that case, otherwise it prints '?'. If x is not equal to y, it also prints '?'. The function does not take any parameters and does not return any value.

