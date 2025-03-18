#State of the program right berfore the function call: a and b are non-negative integers with no more than 10^6 digits.**
def func_1():
    data = input().split()
    a = data[0].lstrip('0')
    b = data[1].lstrip('0')
    if (not a) :
        a = '0'
    #State of the program after the if block has been executed: *`a` is a non-negative integer with no leading zeros, `b` is a non-negative integer with no more than 10^6 digits, `data` is a list containing the input values and `b` is the value of `data[1]` with leading zeros removed. If `a` evaluates to False (a string '0'), then the current value of `a` becomes False.
    if (not b) :
        b = '0'
    #State of the program after the if block has been executed: *`a` is a non-negative integer with no leading zeros, `b` is a non-negative integer with no more than 10^6 digits, `data` is a list containing the input values, `b` is the value of `data[1]` with leading zeros removed. If `a` evaluates to False (a string '0'), then the current value of `a` becomes False. If `b` is 0, then the value of `a` remains unchanged.
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
                #State of the program after the if-else block has been executed: *`a` is a non-negative integer with no leading zeros, `b` is a non-negative integer with no more than 10^6 digits, `data` is a list containing the input values, `b` is the value of `data[1]` with leading zeros removed. If `a` evaluates to False (a string '0'), then the current value of `a` becomes False. If `b` is 0, then the value of `a` remains unchanged. The length of `a` is greater than or equal to the length of `b`. The length of `a` is not greater than the length of `b`. `a` is greater than or equal to `b`. If the condition (a > b) is true, then the current value of `a` is greater than `b`. Otherwise, `a` is not greater than `b`.
            #State of the program after the if-else block has been executed: *`a` is a non-negative integer with no leading zeros, `b` is a non-negative integer with no more than 10^6 digits, `data` is a list containing the input values, `b` is the value of `data[1]` with leading zeros removed. If `a` evaluates to False (a string '0'), then the current value of `a` becomes False. If `b` is 0, then the value of `a` remains unchanged. The length of `a` is greater than or equal to the length of `b`. The length of `a` is not greater than the length of `b`. If the condition (a < b) is true, then the current value of `a` is less than `b` and the code prints '<'. If the condition (a >= b) is true, then the current value of `a` is greater than or equal to `b`.
        #State of the program after the if-else block has been executed: *`a` is a non-negative integer with no leading zeros, `b` is a non-negative integer with no more than 10^6 digits, `data` is a list containing the input values, `b` is the value of `data[1]` with leading zeros removed. If `a` evaluates to False (a string '0'), then the current value of `a` becomes False. If `b` is 0, then the value of `a` remains unchanged. The length of `a` is greater than or equal to the length of `b`. The current value of `a` is such that the length of `a` is greater than the length of `b`. If the condition (a < b) is true, then the current value of `a` is less than `b` and the code prints '<'. If the condition (a >= b) is true, then the current value of `a` is greater than or equal to `b`.
    #State of the program after the if-else block has been executed: *`a` is a non-negative integer with no leading zeros and `b` is a non-negative integer with no more than 10^6 digits. If the length of `a` is less than the length of `b`, `a` is less than `b` and the code prints '<'. If the length of `a` is greater than or equal to the length of `b`, `a` is greater than or equal to `b` and the code prints '>'. If the length of `a` is greater than the length of `b` and a < b is true, then the current value of `a` is less than `b` and the code prints '<'. If a >= b, the current value of `a` is greater than or equal to `b`. If `a` evaluates to False (a string '0'), then the current value of `a` becomes False. If `b` is 0, then the value of `a` remains unchanged.
#Overall this is what the function does:The function `func_1` does not accept any parameters. It reads input values for two non-negative integers `a` and `b`, removing leading zeros if present. Then, it compares the lengths of `a` and `b`, printing '<' if `a` is less than `b`, '>', if `a` is greater than `b`, and '=' if they are equal. The functionality of the function is to compare and print the relationship between two non-negative integers `a` and `b`, handling cases where `a` or `b` evaluates to '0' and scenarios where the lengths of `a` and `b` are different.

