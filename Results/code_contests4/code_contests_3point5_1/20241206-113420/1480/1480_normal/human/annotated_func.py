#State of the program right berfore the function call: a, b, and x are integers such that 1 ≤ a, b ≤ 100, and 1 ≤ x < a + b.**
def func():
    a, b, x = map(int, raw_input().split(' '))
    if (x > 1 and a == 1) :
        s = '1'
        b -= 1
    else :
        s = '0'
        a -= 1
    #State of the program after the if-else block has been executed: *`a`, `b`, `x` are integers such that 1 ≤ a, b ≤ 100 and 1 ≤ x < a + b. If x > 1 and a == 1, then a is 1, b is an integer such that 1 ≤ b - 1 ≤ 99, x is an integer such that 1 ≤ x < a + b, `s` is a string '1'. If x ≤ 1 or a ≠ 1, then a is decreased by 1, b is an integer such that 1 ≤ b ≤ 100, x is an integer such that 1 ≤ x < a + b, `s` is assigned the string '0'.
    while x > 1:
        if s[-1] == '0':
            s += '1'
            b -= 1
        else:
            s += '0'
            a -= 1
        
        x -= 1
        
    #State of the program after the loop has been executed: `a` is an integer between 1 and 100, `b` is an integer, `s` is a string. If the last character of `s` is '1', '0' is appended to `s`, `a` is decremented by a total number of times equal to the original value of `x`, `b` is decreased by a total number of times equal to the original value of `x`, `x` is 1. If the last character of `s` is '0', `a` is decremented by a total number of times equal to the original value of `x` minus 1, `b` is decreased by a total number of times equal to the original value of `x` minus 1, `x` is 1
    if (s[-1] == '0') :
        s += '1' * b
        s += '0' * a
    else :
        s += '0' * a
        s += '1' * b
    #State of the program after the if-else block has been executed: *`a` is an integer between 1 and 100, `b` is an integer, `s` is a string. If the last character of `s` is '1', '0' is appended to `s`, `a` is decremented by a total number of times equal to the original value of `x`, `b` is decreased by a total number of times equal to the original value of `x`, `x` is 1. If the last character of `s` is '0', `a` is decremented by a total number of times equal to the original value of `x` minus 1, `b` is decreased by a total number of times equal to the original value of `x` minus 1, `x` is 1. If the last character of `s` is '0', `a` is decremented by a total number of times equal to the original value of `x` minus 1, `b` is decreased by a total number of times equal to the original value of `x` minus 1, `x` is 1. If the last character of `s` is '1', '0' is appended to `s`, `a` is decremented by a total number of times equal to the original value of `x`, `b` is decreased by a total number of times equal to the original value of `x`, `x` is 1
    print(s)
#Overall this is what the function does:The function `func` reads three integers a, b, and x from input, and based on certain conditions, it constructs a string `s`. The function then prints the final string `s` based on the conditions. If x is greater than 1 and a is 1, then '1' is appended to `s` and b is decremented. If x is less than or equal to 1 or a is not 1, '0' is appended to `s` and a is decremented. The loop continues to append alternately '1' and '0' to `s` based on specific conditions until x becomes 1. After the loop, '1' and '0' are appended to `s` based on the last character of `s` to form the final string. The function prints the constructed string `s`.

