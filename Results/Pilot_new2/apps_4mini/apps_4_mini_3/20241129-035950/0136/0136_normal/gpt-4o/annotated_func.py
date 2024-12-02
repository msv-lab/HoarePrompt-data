#State of the program right berfore the function call: a and b are non-negative integers represented as strings, each string may contain leading zeroes and has a length of at most 10^6 characters.
def func_1():
    data = input().split()
    a = data[0].lstrip('0')
    b = data[1].lstrip('0')
    if (not a) :
        a = '0'
    #State of the program after the if block has been executed: *`a` is the string representation of the integer value of `data[0]` with leading zeros removed. If `a` is empty, then `a` is '0' and `b` remains the string representation of `data[1]` with leading zeros removed. There is no change to the list `data` which remains as a list of strings obtained from splitting the input.
    if (not b) :
        b = '0'
    #State of the program after the if block has been executed: *`a` is the string representation of the integer value of `data[0]` with leading zeros removed, or '0' if `a` is empty. If `b` is empty, then `b` is set to '0', and `data` remains unchanged as a list of strings obtained from splitting the input.
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
                #State of the program after the if-else block has been executed: *`a` is the string representation of the integer value of `data[0]` with leading zeros removed or '0' if `a` is empty; `b` is '0' if empty; `data` remains unchanged as a list of strings obtained from splitting the input; the length of `a` is equal to the length of `b`; and `a` is greater than or equal to `b`. If `a` is greater than `b`, the output '>' is printed. Otherwise, if `a` is less than or equal to `b`, the output '=' is printed.
            #State of the program after the if-else block has been executed: *`a` is the string representation of the integer value of `data[0]` with leading zeros removed, or '0' if `a` is empty; `b` is '0' if `b` is empty; `data` remains unchanged as a list of strings obtained from splitting the input; the length of `a` is equal to the length of `b`. If `a` is less than `b`, the output is '<'. If `a` is greater than `b`, the output is '>'. Otherwise, if `a` is equal to `b`, the output is '='.
        #State of the program after the if-else block has been executed: *`a` is the string representation of the integer value of `data[0]` with leading zeros removed, or '0' if `a` is empty; `b` is '0' if it was empty; `data` remains unchanged as a list of strings obtained from splitting the input; if the length of `a` is greater than the length of `b`, '>' is printed to the output. If the lengths are equal, the outputs are determined by comparing `a` and `b`: if `a` is less than `b`, '<' is printed; if `a` is greater than `b`, '>' is printed; otherwise, '=' is printed.
    #State of the program after the if-else block has been executed: *`a` is the string representation of the integer value of `data[0]` with leading zeros removed, or '0' if `a` is empty; `b` is '0' if it was empty; `data` remains unchanged as a list of strings obtained from splitting the input. If the length of `a` is less than the length of `b`, '<' is printed. If the length of `a` is greater than the length of `b`, '>' is printed. If the lengths are equal, the outputs are determined by comparing `a` and `b`: if `a` is less than `b`, '<' is printed; if `a` is greater than `b`, '>' is printed; otherwise, '=' is printed.
#Overall this is what the function does:The function accepts two non-negative integers `a` and `b` in string format, removes any leading zeros, and compares their values. It prints '<' if `a` is less than `b`, '>' if `a` is greater than `b`, or '=' if they are equal. If either string is empty after removing leading zeros, it is treated as '0'. The function is designed to handle very large integers represented as strings, up to a length of 10^6 characters.

