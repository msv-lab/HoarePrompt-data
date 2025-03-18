#State of the program right berfore the function call: a and b are non-negative integers represented as strings, each containing at most 10^6 digits, and may have leading zeroes.
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
        #State of the program after the if-else block has been executed: *`a` and `b` are non-negative integers represented as strings without leading zeros, `a` is not equal to `b`, if `a` is less than `b`, then the string `<` has been printed; otherwise, the string `>` has been printed.
    #State of the program after the if-else block has been executed: *`a` and `b` are non-negative integers represented as strings without leading zeros. If `a` is equal to `b`, then the current value of `a` is equal to the current value of `b`. If `a` is not equal to `b`, the function checks their values: if `a` is less than `b`, the string `<` has been printed; otherwise, the string `>` has been printed.
#Overall this is what the function does:The function accepts two non-negative integers represented as strings, each potentially containing leading zeros and up to 10^6 digits. It compares the two integers after stripping leading zeros and prints '=' if they are equal, '<' if the first integer is less than the second, or '>' if the first integer is greater than the second.

