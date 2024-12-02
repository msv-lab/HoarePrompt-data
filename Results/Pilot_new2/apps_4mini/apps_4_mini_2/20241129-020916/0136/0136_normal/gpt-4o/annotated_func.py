#State of the program right berfore the function call: a and b are two non-negative integers represented as strings, which may contain leading zeroes, and each can have up to 10^6 digits.
def func_1():
    data = input().split()
    a = data[0].lstrip('0')
    b = data[1].lstrip('0')
    if (not a) :
        a = '0'
    #State of the program after the if block has been executed: *`a` is the string representation of `data[0]` without leading zeroes, and if `a` is '0', then `b` is a non-negative integer represented as a string after leading zeroes are stripped from `data[1]`, while `data` remains a list of strings containing the input split by whitespace.
    if (not b) :
        b = '0'
    #State of the program after the if block has been executed: *`a` is the string representation of `data[0]` without leading zeroes, if `a` is '0', then `b` is '0'; `data` remains a list of strings containing the input split by whitespace, and the current value of `b` is '0'.
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
                #State of the program after the if-else block has been executed: *`a` is the string representation of `data[0]` without leading zeroes, if `a` is '0', then `b` is '0'; `data` remains a list of strings containing the input split by whitespace, and the current value of `b` is '0'. The length of `a` is equal to the length of `b`, if `a` is greater than `b`, then `a` is confirmed to be greater than `b`. Otherwise, if `a` is less than or equal to `b`, the output printed is '='.
            #State of the program after the if-else block has been executed: *`a` is the string representation of `data[0]` without leading zeroes, if `a` is '0', then `b` is '0'; `data` remains a list of strings containing the input split by whitespace, and the current value of `b` is '0'. The length of `a` is equal to the length of `b`. If `a` is less than `b`, then `a` is confirmed to be less than `b`. If `a` is greater than `b`, then `a` is confirmed to be greater than `b`. Otherwise, if `a` is less than or equal to `b`, the output printed is '='.
        #State of the program after the if-else block has been executed: *`a` is the string representation of `data[0]` without leading zeroes, if `a` is '0', then `b` is '0'; `data` remains a list of strings containing the input split by whitespace, and the current value of `b` is '0'. If the length of `a` is greater than the length of `b`, the printed output is '>'. If the length of `a` is equal to the length of `b`, then if `a` is less than `b`, it is confirmed that `a` is less than `b`; if `a` is greater than `b`, it is confirmed that `a` is greater than `b`; otherwise, if `a` is less than or equal to `b`, the printed output is '='.
    #State of the program after the if-else block has been executed: *`a` is the string representation of `data[0]` without leading zeroes, if `a` is '0', then `b` is '0'; `data` remains a list of strings containing the input split by whitespace, and the current value of `b` is '0'. If the length of `a` is less than the length of `b`, the output is '<'. If the length of `a` is greater than the length of `b`, the output is '>'. If the lengths of `a` and `b` are equal, then if `a` is less than `b`, the output is confirmed as '<'; if `a` is greater than `b`, the output is confirmed as '>'; otherwise, the output is '='.
#Overall this is what the function does:The function accepts two non-negative integers represented as strings, `a` and `b`, which may contain leading zeroes, and compares them. It outputs '<' if `a` is less than `b`, '>' if `a` is greater than `b`, and '=' if they are equal. If either `a` or `b` is an empty string after stripping leading zeroes, it is treated as '0'. The function does not return any value; it only prints the comparison result.

