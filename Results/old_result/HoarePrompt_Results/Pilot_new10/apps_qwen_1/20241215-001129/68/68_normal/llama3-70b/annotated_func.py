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
                #State of the program after the if-else block has been executed: `x` and `y` are integers in the range 0 <= x, y <= 100, and `x` is equal to `y`. If `z` is 0, then no change is made to `x` and `y`. If `z` is not 0, then `x` and `y` remain equal, but this equality is already established before the if-else block executes.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *`x` and `y` are integers in the range 0 <= x, y <= 100, and `x` is greater than or equal to `y`. If `z` is 0, `x` and `y` remain unchanged. If `z` is not 0, `x` and `y` remain equal. Regardless of the value of `z`, `x` is unchanged from its initial state.
        #State of the program after the if-else block has been executed: *`x` and `y` are integers in the range 0 <= x, y, z <= 100. If `x` is less than `y`, then `x` remains less than or equal to `y + z` and `x` is unchanged. If `x` is greater than or equal to `y`, then either `x` and `y` remain equal (if `z` is 0) or `x` remains unchanged (if `z` is not 0). In both cases, `x` remains within its initial range and satisfies the condition `x <= y + z`.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers in the range 0 <= x, y, z <= 100. If `x` is greater than the sum of `y` and `z`, then `x` remains greater than the sum of `y` and `z`. Otherwise, `x` remains less than or equal to the sum of `y` and `z`, and the values of `x`, `y`, and `z` do not change beyond their initial ranges.
#Overall this is what the function does:The function does not accept any parameters but expects three non-negative integers \( x \), \( y \), and \( z \) within the range 0 to 100 from user input. It prints '+' if \( x \) is greater than the sum of \( y \) and \( z \); it prints '-' if \( x \) is less than \( y \); it prints '0' if \( x \) equals \( y \) and \( z \) is 0; it prints '?' if \( x \) equals \( y \) and \( z \) is not 0; and it prints '?' if \( x \) is greater than or equal to \( y \) but not necessarily greater than the sum of \( y \) and \( z \).

