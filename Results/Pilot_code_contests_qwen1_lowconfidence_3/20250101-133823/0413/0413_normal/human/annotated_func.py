#State of the program right berfore the function call: The input consists of four lines. The first line contains two space-separated integers n and bx (1 ≤ n ≤ 10, 2 ≤ bx ≤ 40), where n is the number of digits in the bx-based representation of X. The second line contains n space-separated integers x1, x2, ..., xn (0 ≤ xi < bx) — the digits of X. The third line contains two space-separated integers m and by (1 ≤ m ≤ 10, 2 ≤ by ≤ 40, bx ≠ by), where m is the number of digits in the by-based representation of Y. The fourth line contains m space-separated integers y1, y2, ..., ym (0 ≤ yi < by) — the digits of Y. There will be no leading zeroes, and both X and Y will be positive. All digits of both numbers are given in the standard decimal numeral system.
def func():
    s = raw_input().split(' ')
    n = int(s[0])
    bx = int(s[1])
    x = 0
    xs = raw_input().split(' ')
    for i in range(n - 1, -1, -1):
        a = int(xs[n - 1 - i])
        
        x = x + bx ** i * a
        
    #State of the program after the  for loop has been executed: `s` is a list starting with 'n', followed by other elements, `n` is a non-negative integer, `bx` is the integer value of `s[1]`, `x` is the base `bx` representation of the number represented by the list `s[2:]`.
    s = raw_input().split(' ')
    m = int(s[0])
    by = int(s[1])
    y = 0
    ys = raw_input().split(' ')
    for i in range(m - 1, -1, -1):
        a = int(ys[m - 1 - i])
        
        y = y + by ** i * a
        
    #State of the program after the  for loop has been executed: `i` is `-1`, `m` is a non-negative integer, `a` is the integer value of `ys[m]`, `y` is the sum of all elements in `ys` converted from base `by`.
    if (x == y) :
        ans = '='
    else :
        if (x > y) :
            ans = '>'
        else :
            ans = '<'
        #State of the program after the if-else block has been executed: *`i` is -1, `m` is a non-negative integer, `a` is the integer value of `ys[m]`, `y` is the sum of all elements in `ys` converted from base `by`, and `ans` is either '>' if `x` is greater than `y`, or '<' if `x` is less than or equal to `y`.
    #State of the program after the if-else block has been executed: *`i` is -1, `m` is a non-negative integer, `a` is the integer value of `ys[m]`, `y` is the sum of all elements in `ys` converted from base `by`, and `ans` is set to either '=' if `x` equals `y`, '>' if `x` is greater than `y`, or '<' if `x` is less than or equal to `y`.
    print(ans)
#Overall this is what the function does:The function reads two numbers \(X\) and \(Y\) from the user input, where \(X\) is represented in base \(bx\) and \(Y\) is represented in base \(by\). The function then converts both numbers from their respective bases to base 10 and compares them. Based on the comparison, it prints either '<', '=', or '>' indicating whether \(X\) is less than, equal to, or greater than \(Y\) respectively. The function handles the following edge cases: both inputs are valid (1 ≤ n, m ≤ 10, 2 ≤ bx, by ≤ 40, bx ≠ by), no leading zeroes, and the digits are within the valid range (0 ≤ xi, yi < bx, by). If the input does not meet these criteria, the function may produce unexpected results.

