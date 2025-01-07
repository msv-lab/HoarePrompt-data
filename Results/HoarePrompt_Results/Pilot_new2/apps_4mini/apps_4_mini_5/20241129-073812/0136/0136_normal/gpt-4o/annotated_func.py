#State of the program right berfore the function call: a and b are strings representing non-negative integers that may contain leading zeros and have a length of no more than 10^6 digits.
def func_1():
    data = input().split()
    a = data[0].lstrip('0')
    b = data[1].lstrip('0')
    if (not a) :
        a = '0'
    #State of the program after the if block has been executed: *`a` is a string representing a non-negative integer with leading zeros removed, and if `a` is empty, then `a` is '0' and `b` is the string from `data[1]` with leading zeros removed. If `a` is not empty, its value remains unchanged.
    if (not b) :
        b = '0'
    #State of the program after the if block has been executed: *`a` is a string representing a non-negative integer with leading zeros removed. If `b` is empty, then `b` is set to '0', and if `a` was originally empty, it is also set to '0'. If `b` is not empty, its value remains unchanged.
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
                #State of the program after the if-else block has been executed: *`a` is a string representing a non-negative integer with leading zeros removed, `b` is '0' if it was originally empty or retains its value if not empty, and the length of `a` is equal to the length of `b`. If `a` is greater than `b`, then '>' has been printed to the console. If `a` is equal to `b`, then '=' has been printed to the console.
            #State of the program after the if-else block has been executed: *`a` is a string representing a non-negative integer with leading zeros removed, `b` is '0' if it was originally empty or retains its value if not empty, and the length of `a` is equal to the length of `b`. If `a` is less than `b`, then the appropriate action for that condition has been taken. Otherwise, if `a` is greater than `b`, '>' has been printed to the console. If `a` is equal to `b`, then '=' has been printed to the console.
        #State of the program after the if-else block has been executed: *`a` is a string representing a non-negative integer with leading zeros removed, `b` is '0' if it was originally empty or retains its value if not empty, if the length of `a` is greater than the length of `b`, then '>' has been printed to the console. If the lengths are equal, if `a` is less than `b`, then the appropriate action for that condition has been taken; if `a` is greater than `b`, '>' has been printed to the console; if `a` is equal to `b`, then '=' has been printed to the console.
    #State of the program after the if-else block has been executed: *`a` is a string representing a non-negative integer with leading zeros removed. If the length of `a` is less than the length of `b`, then `b` is either set to '0' if empty or retains its value if not, and if `a` was originally empty, it is also set to '0'. If the length of `a` is greater than the length of `b`, then '>' has been printed to the console. If the lengths are equal, the appropriate action for the comparison between `a` and `b` has been taken: if `a` is less than `b`, the appropriate action for that condition has been taken; if `a` is greater than `b`, '>' has been printed to the console; if `a` is equal to `b`, then '=' has been printed to the console.
#Overall this is what the function does:The function accepts two strings `a` and `b` that represent non-negative integers, possibly with leading zeros, and compares them. It prints '<' if `a` is less than `b`, '>' if `a` is greater than `b`, and '=' if they are equal. If either `a` or `b` is an empty string, they are treated as '0'. The function also handles cases where the lengths of the strings are different. If both strings are empty, they are both considered as '0', and '=' is printed. However, the function does not return any value; it only prints the result of the comparison.

