#State of the program right berfore the function call: a, b, and x are integers such that 1 ≤ a, b ≤ 100 and 1 ≤ x < a + b.
def func():
    a, b, x = map(int, raw_input().split(' '))
    if (x > 1 and a == 1) :
        s = '1'
        b -= 1
    else :
        s = '0'
        a -= 1
    #State of the program after the if-else block has been executed: *`a`, `b`, and `x` are integers such that 1 ≤ a, b ≤ 100 and 1 ≤ x < a + b. If `x` > 1 and `a` is 1, then `b` is an integer such that 1 ≤ b < 100, `x` is an integer such that 1 ≤ x < 1 + b, and `s` is set to '1'. Otherwise, `a` is decremented by 1, `b` remains unchanged, `x` remains unchanged, and `s` is set to '0'.
    while x > 1:
        if s[-1] == '0':
            s += '1'
            b -= 1
        else:
            s += '0'
            a -= 1
        
        x -= 1
        
    #State of the program after the loop has been executed: `x` is 1, `s` is updated based on the number of iterations (which is `x - 1`), `a` and `b` are decremented accordingly based on the last character of `s` during the iterations. Final values of `a` and `b` depend on the initial conditions and the behavior of `s` through the loop iterations.
    if (s[-1] == '0') :
        s += '1' * b
        s += '0' * a
    else :
        s += '0' * a
        s += '1' * b
    #State of the program after the if-else block has been executed: *`x` is 1, if the last character of `s` is '0', then `s` is updated to '0' * `a`, where `s` was previously empty. Otherwise, `s` is updated by appending '1' repeated `b` times, where `s` remains unchanged from its previous state. The final values of `a` and `b` depend on the initial conditions and the behavior of `s` through the loop iterations.
    print(s)
#Overall this is what the function does:The function accepts three integers a, b, and x, where 1 ≤ a, b ≤ 100 and 1 ≤ x < a + b. It constructs a binary string s based on the values of a, b, and x. If x > 1 and a is 1, it starts s with '1' and decrements b; otherwise, it starts with '0' and decrements a. It then continues to build the string until x is reduced to 1, alternating between appending '1's and '0's based on the last character of s, while decrementing a or b accordingly. Finally, it appends the remaining '1's or '0's based on the last character of s until all a and b are used up. The result is printed as the final binary string.

