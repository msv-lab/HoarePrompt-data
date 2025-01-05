#State of the program right berfore the function call: a and b are integers such that 1 ≤ a, b ≤ 100, and x is an integer such that 1 ≤ x < a + b.
def func():
    a, b, x = map(int, raw_input().split(' '))
    if (x > 1 and a == 1) :
        s = '1'
        b -= 1
    else :
        s = '0'
        a -= 1
    #State of the program after the if-else block has been executed: *`a`, `b`, and `x` are integers. If `x` is greater than 1 and `a` is equal to 1, then `b` is decreased by 1 and `s` is set to '1'. Otherwise, `a` is decreased by 1, `b` remains as the input integer, `x` is the input integer, and `s` is set to '0'.
    while x > 1:
        if s[-1] == '0':
            s += '1'
            b -= 1
        else:
            s += '0'
            a -= 1
        
        x -= 1
        
    #State of the program after the loop has been executed: `x` is 1, `a` and `b` are integers that have been decremented based on the loop execution, and `s` is a string that has been built through the loop iterations.
    if (s[-1] == '0') :
        s += '1' * b
        s += '0' * a
    else :
        s += '0' * a
        s += '1' * b
    #State of the program after the if-else block has been executed: *`x` is 1, `a` is an integer, `b` is an integer. If the last character of `s` is '0', then `s` consists of '1' repeated `b` times followed by '0' repeated `a + 1` times. Otherwise, `s` is the original string concatenated with '1' repeated `b` times and '0' repeated `a` times.
    print(s)
#Overall this is what the function does:The function accepts three integers `a`, `b`, and `x`, where `1 ≤ a, b ≤ 100` and `1 ≤ x < a + b`. It builds a binary string `s` based on the values of `a`, `b`, and `x`. If `x` is greater than 1 and `a` equals 1, the string starts with '1' and `b` is decremented. Otherwise, it starts with '0' and `a` is decremented. The function then alternates between appending '1's and '0's to `s` based on the last character of `s`, until `x` reaches 1. Finally, it appends the remaining '1's and '0's based on the last character in `s` and prints the final string. The function does not handle cases where `x` equals 1 or where `a` or `b` reach negative values due to decrements.

