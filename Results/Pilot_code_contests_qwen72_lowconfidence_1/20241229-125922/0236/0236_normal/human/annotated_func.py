#State of the program right berfore the function call: a and b are non-negative integers such that 0 ≤ a, b ≤ 105 and a + b ≥ 1.
def func_1():
    a, b = map(int, raw_input().split())
    if (not a or not b) :
        stdout.write(str(a * a - b * b) + '\n')
        stdout.write('o' * a + 'x' * b)
        return
        #The program returns None.
    #State of the program after the if block has been executed: *`a` and `b` are non-negative integers such that 0 ≤ a, b ≤ 105 and a + b ≥ 1, and `a`, `b` are updated to the values provided by the user input. Both `a` and `b` are non-zero.
    ans = -10 ** 17
    v = 0
    for i in xrange(1, a + 1):
        x, y = divmod(b, i + 1)
        
        t = i - 1 + (a - i + 1) * (a - i + 1) - y * (x + 1) * (x + 1) - (i + 1 - y
            ) * x * x
        
        if ans < t:
            ans = t
            v = i
        
    #State of the program after the  for loop has been executed: `a` and `b` are non-negative integers such that 0 ≤ a, b ≤ 105 and a + b ≥ 1, both `a` and `b` are non-zero. `v` is the value of `i` that maximizes `t` during the loop execution, or remains 0 if no such `i` exists. `ans` is the maximum value of `t` calculated during the loop, or remains -10000000000000000000 if no such `t` is found. `i` is `a`, the final value of the loop counter. For each `i` from 1 to `a`, `x` and `y` are the quotient and remainder of `b` divided by `i + 1`, respectively. `t` is calculated as `i - 1 + (a - i + 1) * (a - i + 1) - y * (x + 1) * (x + 1) - (i + 1 - y) * x * x`.
    x, y = divmod(b, v + 1)
    c = ['o'] * (v - 1) + ['o' * (a - v + 1)]
    d = ['x' * (x + 1)] * y + ['x' * x] * (a + 1 - y)
    e = []
    for j in xrange(v):
        e.append(d[j])
        
        e.append(c[j])
        
    #State of the program after the  for loop has been executed: `a` and `b` are non-negative integers such that \(0 \leq a, b \leq 105\) and \(a + b \geq 1\), both `a` and `b` are non-zero, `v` is the value of `i` that maximizes `t` during the loop execution or remains 0 if no such `i` exists, `ans` is the maximum value of `t` calculated during the loop or remains -10000000000000000000 if no such `t` is found, `i` is `a`, `x` is the quotient of `b` divided by `v + 1`, `y` is the remainder of `b` divided by `v + 1`, `c` is a list with `v - 1` elements, each being `'o'`, followed by one element which is `'o'` repeated `a - v + 1` times, `d` is a list with `y` elements, each being the string `'x'` repeated `(x + 1)` times, followed by `a + 1 - y` elements, each being the string `'x'` repeated `x` times, `e` is a list containing `v` elements from `d` and `v` elements from `c` in the order they were appended.
    e.append(d[-1])
    stdout.write(str(ans) + '\n')
    stdout.write(''.join(e))
#Overall this is what the function does:The function reads two non-negative integers `a` and `b` from the user input, where \(0 \leq a, b \leq 105\) and \(a + b \geq 1\). If either `a` or `b` is zero, it prints the result of \(a^2 - b^2\) followed by a string consisting of `a` 'o' characters and `b` 'x' characters. If both `a` and `b` are non-zero, it calculates a value `ans` and an index `v` that maximize a specific formula involving `a` and `b`. It then constructs a string `e` by alternating segments of 'o' and 'x' characters based on the value of `v` and the quotient and remainder of `b` divided by `v + 1`. Finally, it prints `ans` followed by the constructed string `e`. The function always returns `None`.

