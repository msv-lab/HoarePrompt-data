#State of the program right berfore the function call: a and b are non-negative integers with no more than 10^6 digits.**
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
        #State of the program after the if-else block has been executed: *`a` and `b` are non-negative integers with no leading zeros and `a` is not equal to `b`. If `a` is less than `b`, the output is '<', otherwise `a` is greater than or equal to `b`.
    #State of the program after the if-else block has been executed: *`a` and `b` are non-negative integers with no leading zeros. If `a` is equal to `b`, the program prints '='. If `a` is not equal to `b`, then if `a` is less than `b`, the program prints '<', otherwise `a` is greater than or equal to `b`.
#Overall this is what the function does:The function `func` reads two non-negative integers `a` and `b` (with no leading zeros) as input. It then compares `a` and `b` and prints '=' if they are equal. If they are not equal, it prints '<' if `a` is less than `b`, and '>' if `a` is greater than or equal to `b`. However, it's important to note that the annotations state that `a` and `b` are non-negative integers with no more than 10^6 digits, but there is no explicit handling of such large numbers in the code. Also, the code does not specify any return values, so the functionality is limited to the comparison and print operations described.

