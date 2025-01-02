#State of the program right berfore the function call: n and m are integers such that 1 ≤ n ≤ 10, 2 ≤ bx ≤ 40, 1 ≤ m ≤ 10, and 2 ≤ by ≤ 40 with bx ≠ by. The second line contains n integers x1, x2, ..., xn representing the digits of X in base bx, and the fourth line contains m integers y1, y2, ..., ym representing the digits of Y in base by. Both x1 and y1 are guaranteed not to be zero, and all digits are in the range 0 ≤ xi < bx and 0 ≤ yi < by.
def func():
    s = raw_input().split(' ')
    n = int(s[0])
    bx = int(s[1])
    x = 0
    xs = raw_input().split(' ')
    for i in range(n - 1, -1, -1):
        a = int(xs[n - 1 - i])
        
        x = x + bx ** i * a
        
    #State of the program after the  for loop has been executed: Output State: `n` is a non-negative integer, `x` is the sum of the weighted integers from `xs` with weights given by powers of `bx`, `m` is an integer such that 1 ≤ `m` ≤ 10, `y` is a list of `m` integers, `bx` is the integer value of `s[1]`, `by` is between 2 and 40, `x1` and `y1` are not zero, `xs` is a list of strings split from the input line.
    s = raw_input().split(' ')
    m = int(s[0])
    by = int(s[1])
    y = 0
    ys = raw_input().split(' ')
    for i in range(m - 1, -1, -1):
        a = int(ys[m - 1 - i])
        
        y = y + by ** i * a
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer; `x` is the sum of the weighted integers from `xs` with weights given by powers of `bx`; `m` is an integer such that `m >= 1`; `y` is the sum of the weighted integers from `ys` with weights given by powers of `by`.
    if (x == y) :
        ans = '='
    else :
        if (x > y) :
            ans = '>'
        else :
            ans = '<'
        #State of the program after the if-else block has been executed: *`n` is a non-negative integer, `x` is the sum of the weighted integers from `xs` with weights given by powers of `bx`, `m` is an integer such that `m >= 1`, `y` is the sum of the weighted integers from `ys` with weights given by powers of `by`, `ans` is either `'>'` or `'<'` depending on whether the sum of the weighted integers from `xs` with weights given by powers of `bx` is greater than or less than the sum of the weighted integers from `ys` with weights given by powers of `by`.
    #State of the program after the if-else block has been executed: *`n` is a non-negative integer, `x` is the sum of the weighted integers from `xs` with weights given by powers of `bx`, `m` is an integer such that `m >= 1`, `y` is the sum of the weighted integers from `ys` with weights given by powers of `by`, and `ans` is either `'='`, `'>'`, or `'<'` depending on the comparison between `x` and `y`.
    print(ans)
#Overall this is what the function does:The function reads two sets of integers representing digits of numbers in different bases from standard input, converts these digit sequences into their corresponding numerical values, and then compares these values. It outputs either '>', '=', or '<' indicating whether the first number is greater than, equal to, or less than the second number. The function handles potential edge cases such as ensuring the base values are within valid ranges (2 ≤ bx ≤ 40 and 2 ≤ by ≤ 40) and that the first digits of each number sequence are not zero. However, it does not handle cases where the input bases are invalid (i.e., outside the specified range), which could lead to errors or unexpected behavior. Additionally, the function assumes the input is well-formed and does not check for non-integer inputs or other forms of malformed data.

