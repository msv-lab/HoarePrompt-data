#State of the program right berfore the function call: a and b are non-negative integers represented as strings with no more than 10^6 digits.**
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
        #State of the program after the if-else block has been executed: *`a` is a non-negative integer represented as a string with no leading zeros, `b` is the input string after removing any leading zeros. `a` is not equal to `b`. If the current value of `a` is less than `b`, the program prints '<'. If the current value of `a` is greater than or equal to `b`, the program prints '>'.
    #State of the program after the if-else block has been executed: *`a` is a non-negative integer represented as a string with no leading zeros, `b` is the input string after removing any leading zeros. If `a` equals `b`, then `a` is equal to `b`. If `a` is not equal to `b`, and `a` is less than `b`, the program prints '<'. If `a` is not equal to `b`, and `a` is greater than or equal to `b`, the program prints '>'.
#Overall this is what the function does:The function `func` reads two non-negative integers represented as strings with no leading zeros, `a` and `b`, from the user input. It then compares `a` and `b` and prints '=' if they are equal. If `a` is less than `b`, it prints '<', and if `a` is greater than or equal to `b`, it prints '>'. The function does not explicitly return any value.

