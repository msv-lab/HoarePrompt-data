#State of the program right berfore the function call: a and b are non-negative integers represented as strings, each containing at most 10^6 digits, and may include leading zeroes.
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
        #State of the program after the if-else block has been executed: *`a` is the string representation of a non-negative integer without leading zeros, and `b` is the input string after removing leading zeros. If `a` is less than `b`, the output is '<'. Otherwise, since `a` is not equal to `b` and is greater than or equal to `b`, the output is '>'
    #State of the program after the if-else block has been executed: *`a` is the string representation of a non-negative integer without leading zeros, and `b` is the input string after removing leading zeros. If `a` is equal to `b`, the output confirms their equality. If `a` is less than `b`, the output is '<'. Otherwise, if `a` is greater than `b`, the output is '>'.
#Overall this is what the function does:The function accepts two non-negative integer strings, `a` and `b`, removes any leading zeros, and compares their values. It prints '=' if they are equal, '<' if `a` is less than `b`, or '>' if `a` is greater than `b`. However, it does not return any value; it only outputs the comparison result directly to the console.

