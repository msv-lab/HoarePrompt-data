#State of the program right berfore the function call: a, b, and x are positive integers such that 1 ≤ a, b ≤ 100 and 1 ≤ x < a + b.**
def func():
    a, b, x = map(int, raw_input().split(' '))
    if (x > 1 and a == 1) :
        s = '1'
        b -= 1
    else :
        s = '0'
        a -= 1
    #State of the program after the if-else block has been executed: *`a`, `b`, `x` are positive integers. If `x` > 1 and `a` is 1, then `a` remains 1, `b` becomes one less than its previous value, `x` remains a positive integer greater than 1, and `s` is the string '1'. If `x` is not greater than 1 or `a` is not 1, then `a` is decreased by 1, `b` and `x` are positive integers satisfying the given conditions, and `s` is the string '0'.
    while x > 1:
        if s[-1] == '0':
            s += '1'
            b -= 1
        else:
            s += '0'
            a -= 1
        
        x -= 1
        
    #State of the program after the loop has been executed: If `x` is greater than 1 and `a` is 1, then `a` remains 1, `b` is `x - 2`, `x` is 1, and `s` is a string of length `x` with alternating '1's and '0's. If `x` is not greater than 1 or `a` is not 1, then `a` is 0, `b` is `x - 1`, `x` is 1, and `s` is a string of length `x` with alternating '1's and '0's.
    if (s[-1] == '0') :
        s += '1' * b
        s += '0' * a
    else :
        s += '0' * a
        s += '1' * b
    #State of the program after the if-else block has been executed: *If `x` is greater than 1 and `a` is 1, then `a` remains 1, `b` is `x - 2`, `x` is 1, and `s` is a string of length `x + b + a` with alternating '1's and '0's. If `x` is not greater than 1 or `a` is not 1, then `a` is 0, `b` is `x - 1`, `x` is 1, and `s` is a string of length `x + b + 1` with alternating '1's and '0's.
    print(s)
#Overall this is what the function does:Functionality: The function `func` reads three positive integers `a`, `b`, and `x` from user input. It then constructs a string `s` based on the values of `a`, `b`, and `x`. If `x` is greater than 1 and `a` is 1, `s` is formed with alternating '1's and '0's with length equal to `x + b + a`. If `x` is not greater than 1 or `a` is not 1, `s` is formed similarly but with length `x + b + 1`. Finally, the function prints the constructed string `s`. There are potential issues with the annotations and missing explanations for various cases, so the actual functionality might differ from what is described in the annotations.

