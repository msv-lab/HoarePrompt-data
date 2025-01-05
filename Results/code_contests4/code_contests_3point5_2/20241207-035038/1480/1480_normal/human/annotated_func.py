#State of the program right berfore the function call: a, b, and x are integers such that 1 ≤ a, b ≤ 100, and 1 ≤ x < a + b.**
def func():
    a, b, x = map(int, raw_input().split(' '))
    if (x > 1 and a == 1) :
        s = '1'
        b -= 1
    else :
        s = '0'
        a -= 1
    #State of the program after the if-else block has been executed: *`a`, `b`, `x` are integers such that 1 ≤ `a`, `b` ≤ 100, and 1 ≤ `x` < `a` + `b`. If `x` > 1 and `a` == 1, then `a` becomes 1, `b` decreases by 1, `x` remains greater than 1, and `s` is assigned the string '1'. If the condition (x > 1 and a == 1) is false, then `a` decreases by 1, `b` and `x` remain unchanged, `s` is still '0'.
    while x > 1:
        if s[-1] == '0':
            s += '1'
            b -= 1
        else:
            s += '0'
            a -= 1
        
        x -= 1
        
    #State of the program after the loop has been executed: 'a', 'b' are integers between 0 and 100, 'x' is an integer between 1 and 'a' + 'b' - 1, 's' is either '0', '1' or '10'. If 's[-1]' is '0', then 's' has been concatenated with '1', 'b' is between 0 and 99. If 's[-1]' is not '0', then 'a' is between 0 and 99, 'b' is between 0 and 100.
    if (s[-1] == '0') :
        s += '1' * b
        s += '0' * a
    else :
        s += '0' * a
        s += '1' * b
    #State of the program after the if-else block has been executed: *'a', 'b' are integers between 0 and 100, 'x' is an integer between 1 and 'a' + 'b' - 1, 's' is either '0', '1' or '10'. If 's[-1]' is '0', then 's' has been concatenated with '1' repeated 'b' times and '0' repeated 'a' times. If 's[-1]' is not '0', then 'a' is between 0 and 99, 'b' is between 0 and 100. 's' is concatenated with '0' repeated 'a' times and '1' repeated between 0 and 100 times.
    print(s)
#Overall this is what the function does:The function takes three integers a, b, and x as input, where 1 ≤ a, b ≤ 100, and 1 ≤ x < a + b. It then performs a series of operations based on the values of a, b, and x, and constructs a string 's' accordingly. The constructed string 's' is then printed as the output. The function handles different cases based on the conditions specified in the code.

