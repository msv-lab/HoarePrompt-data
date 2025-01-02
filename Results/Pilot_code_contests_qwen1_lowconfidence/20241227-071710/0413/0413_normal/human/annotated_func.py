#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 10, bx and by are integers such that 2 ≤ bx, by ≤ 40 and bx ≠ by, xi and yi are integers such that 0 ≤ xi < bx and 0 ≤ yi < by for all i.
def func():
    s = raw_input().split(' ')
    n = int(s[0])
    bx = int(s[1])
    x = 0
    xs = raw_input().split(' ')
    for i in range(n - 1, -1, -1):
        a = int(xs[n - 1 - i])
        
        x = x + bx ** i * a
        
    #State of the program after the  for loop has been executed: `n` is an integer value of `s[0]`, \(1 \leq n \leq 10\); `m` is a positive integer such that \(1 \leq m \leq 10\); `bx` is the integer value of `s[1]`, \(2 \leq bx \leq 40\) and `bx` ≠ `by`; `by` is an integer such that \(2 \leq by \leq 40\) and `bx` ≠ `by`; `xi` and `yi` are integers such that \(0 \leq xi < bx\) and \(0 \leq yi < by\) for all `i`; `s` is a list of strings obtained from the input; `x` is the integer value represented by the string `xs` in base `bx`.
    s = raw_input().split(' ')
    m = int(s[0])
    by = int(s[1])
    y = 0
    ys = raw_input().split(' ')
    for i in range(m - 1, -1, -1):
        a = int(ys[m - 1 - i])
        
        y = y + by ** i * a
        
    #State of the program after the  for loop has been executed: `n` is an integer value of `s[0]` (1 ≤ n ≤ 10); `m` is `n` (1 ≤ m ≤ 10); `bx` is the integer value of `s[1]` (2 ≤ bx ≤ 40 and bx ≠ by); `by` is an integer (2 ≤ by ≤ 40 and bx ≠ by); `xi` and `yi` are integers (0 ≤ xi < bx and 0 ≤ yi < by for all i); `s` is a list of strings obtained from the input; `x` is the integer value represented by the string `xs` in base `bx`; `y` is the integer value represented by the list `ys` in base `bx`.
    if (x == y) :
        ans = '='
    else :
        if (x > y) :
            ans = '>'
        else :
            ans = '<'
        #State of the program after the if-else block has been executed: *`n` is an integer value of `s[0]` (1 ≤ n ≤ 10), `m` is `n` (1 ≤ m ≤ 10), `bx` is the integer value of `s[1]` (2 ≤ bx ≤ 40 and bx ≠ by), `by` is an integer (2 ≤ by ≤ 40 and bx ≠ by), `xi` and `yi` are integers (0 ≤ xi < bx and 0 ≤ yi < by for all i), `s` is a list of strings obtained from the input, `x` is the integer value represented by the string `xs` in base `bx`, `y` is the integer value represented by the list `ys` in base `bx`. After the if-else block, `ans` is `'> '` if `x` is greater than `y`, otherwise `ans` is `'< '` if `x` is less than or equal to `y`.
    #State of the program after the if-else block has been executed: *`n` is an integer value of `s[0]` (1 ≤ n ≤ 10), `m` is `n` (1 ≤ m ≤ 10), `bx` is the integer value of `s[1]` (2 ≤ bx ≤ 40 and bx ≠ by), `by` is an integer (2 ≤ by ≤ 40 and bx ≠ by), `xi` and `yi` are integers (0 ≤ xi < bx and 0 ≤ yi < by for all i), `s` is a list of strings obtained from the input, `x` is the integer value represented by the string `xs` in base `bx`, `y` is the integer value represented by the list `ys` in base `bx`. After the if-else block, `ans` is `'='` if `x` is equal to `y`, `'>'` if `x` is greater than `y`, and `'<'` if `x` is less than `y`.
    print(ans)
#Overall this is what the function does:The function reads two bases and their respective digit representations from the user input, converts them into integers, and compares these integers. The function then outputs one of three characters: '=', '<', or '>', depending on whether the first integer is equal to, less than, or greater than the second integer. The function ensures that `n` and `m` are positive integers within the range [1, 10], `bx` and `by` are integers within the range [2, 40], and `bx` is not equal to `by`. If any of these conditions are violated, the function does not provide an explicit error message but rather focuses on the comparison and output based on valid inputs.

