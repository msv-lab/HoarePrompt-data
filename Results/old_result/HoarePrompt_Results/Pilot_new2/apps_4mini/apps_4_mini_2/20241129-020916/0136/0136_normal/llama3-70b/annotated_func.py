#State of the program right berfore the function call: a and b are non-negative integers represented as strings, with each string potentially containing leading zeroes and having a maximum length of 10^6 digits.
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
        #State of the program after the if-else block has been executed: *`a` and `b` are non-negative integers represented as strings without leading zeroes, and `a` is not equal to `b`. If `a` is less than `b`, then the output `<` is printed to the console. Otherwise, if `a` is greater than or equal to `b`, no output is generated for the comparison.
    #State of the program after the if-else block has been executed: *`a` and `b` are non-negative integers represented as strings without leading zeroes. If `a` is equal to `b`, the output '=' is printed. If `a` is less than `b`, the output '<' is printed. If `a` is greater than `b`, no output is generated for the comparison.
#Overall this is what the function does:The function accepts two non-negative integers represented as strings, reads them from input, and compares their values after stripping leading zeros. It prints '=' if the numbers are equal, '<' if the first number is less than the second, and '>' if the first number is greater than the second. If both inputs are empty or contain only zeros, they will be treated as equal. The function does not handle cases where both inputs are empty strings resulting in an output of '='.

