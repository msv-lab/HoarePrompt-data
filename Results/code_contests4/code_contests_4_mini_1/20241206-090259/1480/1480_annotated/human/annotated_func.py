#State of the program right berfore the function call: a, b, and x are integers such that 1 ≤ a, b ≤ 100 and 1 ≤ x < a + b.
def func():
    a, b, x = map(int, raw_input().split(' '))
    if (x > 1 and a == 1) :
        s = '1'
        b -= 1
    else :
        s = '0'
        a -= 1
    #State of the program after the if-else block has been executed: *`a`, `b`, and `x` are integers satisfying 1 ≤ `a`, `b` ≤ 100 and 1 ≤ `x` < `a` + `b`. If `x` > 1 and `a` is equal to 1, then `b` is decreased by 1, `x` remains unchanged, and `s` is '1'. Otherwise, `a` is decreased by 1, `b` remains unchanged, `x` remains unchanged, and `s` is '0'.
    while x > 1:
        if s[-1] == '0':
            s += '1'
            b -= 1
        else:
            s += '0'
            a -= 1
        
        x -= 1
        
    #State of the program after the loop has been executed: `x` is 1, `a` is decreased by the number of times the loop executed when `s` ended with '0', `b` is decreased by the number of times the loop executed when `s` ended with '1'. The total number of iterations is equal to the initial value of `x` minus 1.
    if (s[-1] == '0') :
        s += '1' * b
        s += '0' * a
    else :
        s += '0' * a
        s += '1' * b
    #State of the program after the if-else block has been executed: *`x` is 1, `a` is decreased by the number of times the loop executed when `s` ended with '0', and `b` is decreased by the number of times the loop executed when `s` ended with '1'. If `s` ends with '0', `s` is updated to '1' * b followed by '0' * a. Otherwise, `s` is appended with '1' * b.
    print(s)
#Overall this is what the function does:The function accepts three integer parameters `a`, `b`, and `x`, where `1 ≤ a, b ≤ 100` and `1 ≤ x < a + b`. It constructs a binary string `s` based on the values of `a`, `b`, and `x`. The string starts with '1' if `x > 1` and `a` is `1`, otherwise it starts with '0'. The function alternates appending '1's and '0's to `s` according to the remaining counts of `a` and `b` after `x` has been decremented to `1`. Finally, it appends any remaining '1's or '0's based on the last character of the string, ensuring the total counts of '1's and '0's correspond to the initial values of `a` and `b`. The resulting binary string is printed.

