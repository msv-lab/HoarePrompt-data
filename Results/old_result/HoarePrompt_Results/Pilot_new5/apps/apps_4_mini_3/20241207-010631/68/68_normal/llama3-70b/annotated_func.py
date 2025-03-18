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
                #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers within the range 0 to 100. If `z` is 0, the output '0' is printed, while `x` is equal to `y`. If `z` is greater than 0, then `x`, `y`, and `z` maintain their relationships such that `x` is less than or equal to the sum of `y` and `z`, and `x` is greater than or equal to `y`, with `x` still equal to `y`.
            else :
                print('?')
            #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers within the range 0 to 100. If `x` is equal to `y`, and if `z` is 0, the output '0' is printed, maintaining that `x` is equal to `y`. If `z` is greater than 0, then `x`, `y`, and `z` retain their relationships such that `x` is less than or equal to the sum of `y` and `z`, and `x` is greater than or equal to `y`. Otherwise, if `x` is not equal to `y`, `x` is still less than or equal to the sum of `y` and `z`, and `x` is greater than or equal to `y` with the additional condition that `x` remains distinct from `y`.
        #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers within the range 0 to 100. If `x` is less than `y`, a '-' is printed. If `x` is equal to `y` and `z` is 0, '0' is printed while maintaining that `x` is equal to `y`. If `z` is greater than 0, then `x`, `y`, and `z` retain their relationships such that `x` is less than or equal to the sum of `y` and `z`, and `x` is greater than or equal to `y`. Otherwise, if `x` is not equal to `y`, `x` remains less than or equal to the sum of `y` and `z`, and `x` is greater than or equal to `y`, ensuring that `x` is distinct from `y`.
    #State of the program after the if-else block has been executed: *`x`, `y`, and `z` are integers within the range 0 to 100. If `x` is greater than `y + z`, the output is '+'. If `x` is less than `y`, a '-' is printed. If `x` is equal to `y` and `z` is 0, '0' is printed while `x` remains equal to `y`. If `z` is greater than 0, then `x` is less than or equal to the sum of `y` and `z` and `x` is greater than or equal to `y`. Otherwise, if `x` is not equal to `y`, `x` remains less than or equal to the sum of `y` and `z`, and `x` is greater than or equal to `y`, ensuring that `x` is distinct from `y`.
#Overall this is what the function does:The function reads three integer inputs, x, y, and z, all of which must be in the range of 0 to 100. It then compares these integers and prints one of the following outputs: '+' if x is greater than the sum of y and z; '-' if x is less than y; '0' if x equals y and z is 0; and '?' in all other cases when x equals y but z is greater than 0, or when x is greater than y but not greater than y + z.

