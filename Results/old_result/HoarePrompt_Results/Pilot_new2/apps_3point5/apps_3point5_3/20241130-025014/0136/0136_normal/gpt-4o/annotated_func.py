#State of the program right berfore the function call: a and b are non-negative integers with no more than 10^6 digits each.**
def func_1():
    data = input().split()
    a = data[0].lstrip('0')
    b = data[1].lstrip('0')
    if (not a) :
        a = '0'
    #State of the program after the if block has been executed: *`a`, `b` are non-negative integers with no leading zeroes. If `a` is '0', `b` is a non-negative integer with no leading zeroes and `a` is False in a boolean context.
    if (not b) :
        b = '0'
    #State of the program after the if block has been executed: *`a`, `b` are non-negative integers with no leading zeroes. If `a` is '0', `b` is '0'. If `b` is not '0', `a` is False in a boolean context.
    if (len(a) < len(b)) :
        print('<')
    else :
        if (len(a) > len(b)) :
            print('>')
        else :
            if (a < b) :
                print('<')
            else :
                if (a > b) :
                    print('>')
                else :
                    print('=')
                #State of the program after the if-else block has been executed: *`a`, `b` are non-negative integers with no leading zeroes. If `a` is '0', `b` is '0'. If `b` is not '0', `a` is False in a boolean context. The length of `a` is greater than or equal to the length of `b`, and the length of `a` is not greater than the length of `b`. The condition (a < b) is false, meaning a is greater than or equal to b. After the execution of the if else block, `a` is either greater than `b` or less than or equal to `b`.
            #State of the program after the if-else block has been executed: *`a`, `b` are non-negative integers with no leading zeroes. If `a` is '0', `b` is '0'. If `b` is not '0', `a` is False in a boolean context. The length of `a` is greater than or equal to the length of `b`, and the length of `a` is not greater than the length of `b`. If `a` is less than `b`, then '<' is printed on the console. If `a` is greater than or equal to `b`, the program does not print anything and `a` is either greater than `b` or less than or equal to `b` after the execution of the if else block.
        #State of the program after the if-else block has been executed: *`a`, `b` are non-negative integers with no leading zeroes. If `a` is '0', `b` is '0'. If `b` is not '0', `a` is False in a boolean context. The length of `a` is greater than or equal to the length of `b`. If the length of `a` is greater than the length of `b`, after the execution of the if else block, the length of `a` remains greater than the length of `b`. If the length of `a` is not greater than the length of `b`, after the execution of the if else block, `a` is either greater than `b` or less than or equal to `b`
    #State of the program after the if-else block has been executed: *`a`, `b` are non-negative integers with no leading zeroes. If `a` is '0', `b` is '0'. If `b` is not '0', `a` is False in a boolean context. If the length of `a` is less than the length of `b`, the output is '<'. If the length of `a` is greater than or equal to the length of `b`, after the execution of the if else block, the length of `a` remains greater than or equal to the length of `b`. If the length of `a` is not greater than the length of `b`, then after the execution of the if else block, `a` is either greater than `b` or less than or equal to `b`.
#Overall this is what the function does:The function `func_1` reads two non-negative integers `a` and `b`, each with no more than 10^6 digits. It then compares the values of `a` and `b` based on their lengths and actual numerical values. If the length of `a` is less than the length of `b`, it prints '<'. If the length of `a` is greater than the length of `b`, it prints '>'. If the lengths are equal, it compares the numerical values of `a` and `b` and prints '<', '>', or '=' accordingly. The function does not return any value.

