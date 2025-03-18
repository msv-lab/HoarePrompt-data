#State of the program right berfore the function call: The function reads two non-negative integers a and b from input, each represented as strings that may contain leading zeroes, and each string can be up to 10^6 digits long.
def func_1():
    data = input().split()
    a = data[0].lstrip('0')
    b = data[1].lstrip('0')
    if (not a) :
        a = '0'
    #State of the program after the if block has been executed: *`data` is a list of length 2 containing two non-negative integers as strings. If `a` is '0', then `b` remains the second element of `data` with leading zeros removed. The else part does not exist in this case.
    if (not b) :
        b = '0'
    #State of the program after the if block has been executed: *`data` is a list of length 2 containing two non-negative integers as strings. If `a` is '0', then `b` is '0'.
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
                #State of the program after the if-else block has been executed: *`data` is a list of length 2 containing two non-negative integers as strings. If `a` is greater than `b`, then `a` is confirmed to be greater than `b`. If `a` is equal to `b`, then the values of `a` and `b` are equal. Furthermore, `a` is '0' if and only if `b` is '0', and the lengths of `a` and `b` are equal.
            #State of the program after the if-else block has been executed: *`data` is a list of length 2 containing two non-negative integers as strings. If `a` is less than `b`, then `a` is confirmed to be less than `b`. If `a` is greater than `b`, then `a` is confirmed to be greater than `b`. If `a` is equal to `b`, then `a` and `b` are equal. Additionally, `a` is '0' if and only if `b` is '0', and the lengths of `a` and `b` remain equal throughout.
        #State of the program after the if-else block has been executed: *`data` is a list of length 2 containing two non-negative integers as strings. If the length of `a` is greater than the length of `b`, then the output is '>'. Otherwise, if the length of `a` is equal to the length of `b`, it is confirmed whether `a` is less than, greater than, or equal to `b`. Additionally, `a` is '0' if and only if `b` is '0', and the lengths of `a` and `b` remain equal throughout.
    #State of the program after the if-else block has been executed: *`data` is a list of length 2 containing two non-negative integers as strings. If the length of `a` is less than the length of `b`, the output '<' has been printed. If the length of `a` is greater than the length of `b`, the output is '>'. If the lengths of `a` and `b` are equal, it is confirmed whether `a` is less than, greater than, or equal to `b`, while ensuring that `a` is '0' if and only if `b` is '0', and the lengths of `a` and `b` remain equal throughout.
#Overall this is what the function does:The function reads two non-negative integers as strings from input, potentially containing leading zeros, and compares them. It prints '<' if the first integer is less than the second, '>' if it is greater, and '=' if they are equal. If either integer is an empty string after removing leading zeros, it is treated as '0'. The function correctly handles cases where the integers are long, up to \(10^6\) digits, but does not return any value; it only prints the comparison result.

