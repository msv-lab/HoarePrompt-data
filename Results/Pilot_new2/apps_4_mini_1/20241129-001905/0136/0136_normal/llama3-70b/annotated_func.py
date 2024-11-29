#State of the program right berfore the function call: a and b are non-negative integers represented as strings, each containing no more than 10^6 digits and may include leading zeroes.
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
        #State of the program after the if-else block has been executed: *`a` and `b` are strings with leading zeros removed; if `a` is less than `b`, the output is '<'. Otherwise, since `a` and `b` are not equal, the output indicates that `a` is greater than or equal to `b`.
    #State of the program after the if-else block has been executed: *`a` is the input string with leading zeros removed and `b` is the input string without leading zeros. If `a` is equal to `b`, the output reflects this equality. If `a` is less than `b`, the output is '<'; otherwise, if `a` is greater than `b`, the output indicates that `a` is greater than or equal to `b.
#Overall this is what the function does:The function accepts two non-negative integer inputs as strings, removes any leading zeroes, and compares the two numbers. It prints '=' if they are equal, '<' if the first number is less than the second, and '>' if the first number is greater than the second. The function does not return any values; it only outputs the comparison result.

