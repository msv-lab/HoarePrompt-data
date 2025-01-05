#State of the program right berfore the function call: a and b are integers in the range [1, 100], and x is an integer in the range [1, a + b - 1].
def func():
    a, b, x = map(int, raw_input().split(' '))
    if (x > 1 and a == 1) :
        s = '1'
        b -= 1
    else :
        s = '0'
        a -= 1
    #State of the program after the if-else block has been executed: *`a` is an integer in the range [1, 100], `b` is an integer in the range [1, 100], and `x` is an integer in the range [1, a + b - 1]. If `x` is greater than 1 and `a` is equal to 1, then `b` is in the range [0, 99] and `s` is set to '1'. Otherwise, `a` is in the range [0, 99], `b` is in the range [1, 100], and `s` is set to '0'.
    while x > 1:
        if s[-1] == '0':
            s += '1'
            b -= 1
        else:
            s += '0'
            a -= 1
        
        x -= 1
        
    #State of the program after the loop has been executed: `x` is 1, `a` is an integer in the range [0, 99], `b` is an integer in the range [0, 99], and `s` is a string of length equal to the initial value of `x` containing a combination of '1's and '0's.
    if (s[-1] == '0') :
        s += '1' * b
        s += '0' * a
    else :
        s += '0' * a
        s += '1' * b
    #State of the program after the if-else block has been executed: *`x` is 1, `a` is an integer in the range [0, 99], and `b` is an integer in the range [0, 99]. If the last character of `s` is '0', then `s` is a string of length 1 plus `b` occurrences of '1' followed by `a` occurrences of '0'. Otherwise, `s` is '1' followed by `a` zeros and then `b` ones.
    print(s)
#Overall this is what the function does:The function accepts two integers `a` and `b` (both in the range [1, 100]) and an integer `x` (in the range [1, a + b - 1]). It constructs a binary string `s` based on the values of `a`, `b`, and `x`. The string starts with either '1' or '0' depending on the conditions of `a` and `x`, and continues by alternating between '1's and '0's until the length of `s` equals `x`. Finally, it appends the remaining '1's and '0's based on the last character of `s`. The output is the constructed binary string.

