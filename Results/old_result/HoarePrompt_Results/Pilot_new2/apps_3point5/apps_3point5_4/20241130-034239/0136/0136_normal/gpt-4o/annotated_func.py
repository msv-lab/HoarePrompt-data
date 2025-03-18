#State of the program right berfore the function call: a and b are non-negative integers with no more than 10^6 digits.**
def func_1():
    data = input().split()
    a = data[0].lstrip('0')
    b = data[1].lstrip('0')
    if (not a) :
        a = '0'
    #State of the program after the if block has been executed: *a, b are non-negative integers with no leading zeros. If a is '0', then 'a' evaluates to False after entering the if condition. Otherwise, there is no change to the values of 'a' and 'b'.
    if (not b) :
        b = '0'
    #State of the program after the if block has been executed: *a, b are non-negative integers with no leading zeros. If 'b' is '0' (string representation of zero), then the function evaluates to False. If 'a' is '0' and 'b' is '0', the function evaluates to False. Otherwise, no change in the values of 'a' and 'b' occurs.
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
                #State of the program after the if-else block has been executed: *'a', 'b' are non-negative integers with no leading zeros. If 'b' is '0', then the function evaluates to False. If 'a' is '0' and 'b' is '0', the function evaluates to False. The length of 'a' is greater than or equal to the length of 'b', and the length of 'a' is not greater than the length of 'b'. The condition (a >= b) is true. If 'a' is greater than 'b', the function will execute the if part, otherwise, it will execute the else part. In the if part, 'a' and 'b' remain unchanged. In the else part, 'a' and 'b' are non-negative integers with no leading zeros. If 'b' is '0', then the function evaluates to False. If 'a' is '0' and 'b' is '0', the function evaluates to False. The length of 'a' is greater than or equal to the length of 'b', and the length of 'a' is not greater than the length of 'b'. The condition (a >= b) is true, and 'a' is not greater than 'b'.
            #State of the program after the if-else block has been executed: *'a', 'b' are non-negative integers with no leading zeros. If 'b' is '0', the function evaluates to False. If 'a' is '0' and 'b' is '0', the function evaluates to False. The length of 'a' is greater than or equal to the length of 'b', and the length of 'a' is not greater than the length of 'b'. If 'a' is less than 'b', no change occurs in 'a' and 'b'. If 'a' is greater than or equal to 'b', 'a' and 'b' are non-negative integers with no leading zeros. If 'b' is '0', then the function evaluates to False. If 'a' is '0' and 'b' is '0', the function evaluates to False. The length of 'a' is greater than or equal to the length of 'b', and the length of 'a' is not greater than the length of 'b'. The condition (a >= b) is true, and 'a' is not greater than 'b'.
        #State of the program after the if-else block has been executed: *'a', 'b' are non-negative integers with no leading zeros. If 'b' is '0', the function evaluates to False. If 'a' is '0' and 'b' is '0', the function evaluates to False. The length of 'a' is greater than or equal to the length of 'b'. If the length of 'a' is greater than the length of 'b', the program executes the if part. If the length of 'a' is not greater than the length of 'b', the program executes the else part. In the if part, the current length of 'a' is greater than the length of 'b' and if 'a' is less than 'b', no change occurs in 'a' and 'b'. If 'a' is greater than or equal to 'b', 'a' and 'b' are non-negative integers with no leading zeros, where 'b' is '0', then the function evaluates to False, and 'a' is not greater than 'b'.
    #State of the program after the if-else block has been executed: *'a', 'b' are non-negative integers with no leading zeros. If 'b' is '0', then the function evaluates to False. If 'a' is '0' and 'b' is '0', the function evaluates to False. The length of 'a' is either less than the length of 'b' or greater than or equal to it. If the length of 'a' is less than the length of 'b', no change occurs in 'a' and 'b'. If the length of 'a' is greater than or equal to the length of 'b', and 'a' is less than 'b', no change occurs in 'a' and 'b'. If 'a' is greater than or equal to 'b', 'a' and 'b' are non-negative integers with no leading zeros. If 'b' is '0', then the function evaluates to False and 'a' is not greater than 'b'.
#Overall this is what the function does:The function reads two non-negative integers, a and b, from input. It removes leading zeros from both a and b. If a is '0', it is converted to the integer 0. If b is '0', it is also converted to the integer 0. It then compares the values of a and b. If a is less than b, it prints '<'. If a is greater than b, it prints '>'. If a is equal to b, it prints '='. The function does not accept any parameters and does not have a specified return value.

