#State of the program right berfore the function call: a, b, and x are integers such that 1 ≤ a, b ≤ 100 and 1 ≤ x < a + b.
def func():
    a, b, x = map(int, raw_input().split(' '))
    if (x > 1 and a == 1) :
        s = '1'
        b -= 1
    else :
        s = '0'
        a -= 1
    #State of the program after the if-else block has been executed: *`a`, `b`, and `x` are integers. If `x` is greater than 1 and `a` is equal to 1, then `b` has been decremented by 1 and `s` is '1'. Otherwise, `a` is decremented by 1, `b` remains an integer, `x` remains an integer, and `s` is '0'.
    while x > 1:
        if s[-1] == '0':
            s += '1'
            b -= 1
        else:
            s += '0'
            a -= 1
        
        x -= 1
        
    #State of the program after the loop has been executed: `x` is 1, `a` is decremented by the number of times `s` ended with '1', `b` is decremented by the number of times `s` ended with '0', `s` will have a length equal to the initial value of `x` minus 1, and `a` and `b` remain integers.
    if (s[-1] == '0') :
        s += '1' * b
        s += '0' * a
    else :
        s += '0' * a
        s += '1' * b
    #State of the program after the if-else block has been executed: *`x` is 1, if `s` ends with '0', then `a` is decremented by the number of times `s` ended with '1' and `b` is decremented by the number of times `s` ended with '0', resulting in `s` being an empty string. Otherwise, `a` is decremented by 1 (i.e., `a` becomes `a_original - 1`), and `s` is updated to '1' followed by `a_original - 1` number of '0's followed by `b` number of '1's.
    print(s)
#Overall this is what the function does:The function accepts three integers `a`, `b`, and `x`, where `1 ≤ a, b ≤ 100` and `1 ≤ x < a + b`. It constructs a binary string `s` of length `x` based on the values of `a`, `b`, and `x`. The string alternates between '1's and '0's, starting with '1' if certain conditions are met, and appending remaining '1's or '0's based on the counts of `a` and `b` after the loop. Finally, the constructed string `s` is printed. The function does not return any value.

