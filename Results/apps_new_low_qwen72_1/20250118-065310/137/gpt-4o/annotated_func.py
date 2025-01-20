#State of the program right berfore the function call: a and b are strings representing non-negative integers, each possibly containing leading zeroes and no more than 10^6 digits.
def func_1():
    data = input().split()

a = data[0].lstrip('0')

b = data[1].lstrip('0')
    if (not a) :
        a = '0'
    #State of the program after the if block has been executed: *`a` is a string representing a non-negative integer without leading zeroes, `b` is a string representing a non-negative integer without leading zeroes. If `a` is an empty string, `a` is considered as '0'.
    if (not b) :
        b = '0'
    #State of the program after the if block has been executed: *`a` is a string representing a non-negative integer without leading zeroes (or `'0'` if `a` is an empty string). If `b` is an empty string, `b` is set to `'0'`.
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
                #State of the program after the if-else block has been executed: *`a` is a string representing a non-negative integer without leading zeroes (or `'0'` if `a` is an empty string). If `b` is an empty string, `b` is set to `'0'`. The length of `a` is greater than or equal to the length of `b`, and the length of `a` is equal to the length of `b`. Additionally, if `a` is greater than `b`, the character `>` has been printed. Otherwise, `a` is equal to `b`.
            #State of the program after the if-else block has been executed: *`a` is a string representing a non-negative integer without leading zeroes (or `'0'` if `a` is an empty string). If `b` is an empty string, `b` is set to `'0'`. The length of `a` is greater than or equal to the length of `b`, and the length of `a` is equal to the length of `b`. If `a` is less than `b`, the program remains in this state. If `a` is greater than `b`, the character `>` has been printed. If `a` is equal to `b`, the program remains in this state.
        #State of the program after the if-else block has been executed: *`a` is a string representing a non-negative integer without leading zeroes (or `'0'` if `a` is an empty string). If `b` is an empty string, `b` is set to `'0'`. The length of `a` is greater than or equal to the length of `b`. If the length of `a` is greater than the length of `b`, '>' is printed. If the lengths of `a` and `b` are equal, and `a` is greater than `b`, '>' is printed. If `a` is less than or equal to `b` and their lengths are equal, the program remains in this state.
    #State of the program after the if-else block has been executed: *`a` is a string representing a non-negative integer without leading zeroes (or `'0'` if `a` is an empty string). If `b` is an empty string, `b` is set to `'0'`. If the length of `a` is less than the length of `b`, the program remains in this state. If the length of `a` is greater than the length of `b`, '>' is printed. If the lengths of `a` and `b` are equal, and `a` is greater than `b`, '>' is printed. If `a` is less than or equal to `b` and their lengths are equal, the program remains in this state.
#Overall this is what the function does:The function reads two strings `a` and `b` from user input, where each string represents a non-negative integer and may contain leading zeroes. It then removes leading zeroes from both `a` and `b`, setting them to '0' if they become empty. The function compares the numerical values of `a` and `b` and prints one of the characters '<', '>', or '=' based on the comparison: '<' if `a` is numerically less than `b`, '>' if `a` is numerically greater than `b`, and '=' if `a` is numerically equal to `b`. The function does not return any value; it only prints the comparison result. Edge cases handled include when either `a` or `b` is an empty string after removing leading zeroes, in which case they are set to '0'. The function assumes valid input where `a` and `b` are strings of non-negative integers up to 10^6 digits long.

