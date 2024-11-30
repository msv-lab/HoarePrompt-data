#State of the program right berfore the function call: a and b are non-negative integers with at most 10^6 digits.**
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
        #State of the program after the if-else block has been executed: *`a` is a non-negative integer with at most 10^6 digits, `b` is a non-negative integer with at most 10^6 digits where `b` is the input string after removing any leading zeros. The value of `a` is not equal to the value of `b`. If `a` is less than `b`, then the program prints '<'. Otherwise, `a` is greater than or equal to `b`.
    #State of the program after the if-else block has been executed: *`a` is a non-negative integer with at most 10^6 digits, `b` is a non-negative integer with at most 10^6 digits where `b` is the input string after removing any leading zeros. If `a` is equal to `b`, then the program does nothing. If `a` is not equal to `b`, the program compares the values. If `a` is less than `b`, then the program prints '<'. Otherwise, `a` is greater than or equal to `b`.
#Overall this is what the function does:The function `func` reads two non-negative integers `a` and `b` with at most 10^6 digits as input. It then compares the values of `a` and `b`. If `a` is equal to `b`, it prints '='. If `a` is less than `b`, it prints '<'. If `a` is greater than or equal to `b`, it prints '>'.

