#State of the program right berfore the function call: a and b are non-negative integers with each containing no more than 10^6 digits.**
def func():
    a = input().lstrip('0')
    b = input().lstrip('0')
    if (a == b) :
        print('=')
    else :
        if (a < b) :
            print('<')
        else :
            print('>')
        #State of the program after the if-else block has been executed: *`a` is a non-negative integer with no leading zeros, `b` is a string with leading zeros removed from the input. If `a` < `b`, the program outputs '<'. Otherwise, if `a` is not equal to `b` and `a` is not less than `b`, the program continues without any output.
    #State of the program after the if-else block has been executed: *`a` is a non-negative integer with no leading zeros, `b` is a string with leading zeros removed from the input. If `a` is equal to `b`, the program does nothing. If `a` < `b`, the program outputs '<'. Otherwise, if `a` is not equal to `b` and `a` is not less than `b`, the program continues without any output.
#Overall this is what the function does:Functionality: The function takes two non-negative integers `a` and `b`, each containing no more than 10^6 digits as input. It compares the values of `a` and `b` after removing leading zeros. If `a` is equal to `b`, it prints '='. If `a` is less than `b`, it prints '<'. If `a` is not equal to `b` and not less than `b`, it continues without any output. It does not calculate the sum of the digits as stated in the annotations. Make sure to handle edge cases where inputs have leading zeros or differ in length.

