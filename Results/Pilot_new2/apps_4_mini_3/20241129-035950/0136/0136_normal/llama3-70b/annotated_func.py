#State of the program right berfore the function call: a and b are non-negative integers represented as strings that may contain leading zeroes, and each string can have at most 10^6 characters.
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
        #State of the program after the if-else block has been executed: *`a` and `b` are non-negative integers represented as strings without leading zeroes and `a` is not equal to `b`. If `a` is less than `b`, the output is '<'. Otherwise, the output indicates that `a` is greater than or equal to `b.
    #State of the program after the if-else block has been executed: *`a` and `b` are non-negative integers represented as strings without leading zeroes. If `a` is equal to `b`, they are equal. If `a` is not equal to `b`, the output indicates that `a` is less than `b` or that `a` is greater than or equal to `b`.
#Overall this is what the function does:The function accepts two non-negative integers represented as strings, compares them after removing any leading zeroes, and prints '=' if they are equal, '<' if the first number is less than the second, or '>' if the first number is greater than the second. It handles cases where the input numbers may have leading zeroes, ensuring accurate comparison. If both inputs are empty strings or consist only of zeroes, they will be treated as equal.

