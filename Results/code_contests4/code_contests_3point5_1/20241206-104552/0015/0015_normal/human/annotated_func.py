#State of the program right berfore the function call: **Precondition**: **n, x, and y are integers such that 1 <= n, x, y <= 104 and x <= n.**
def func():
    c = raw_input()
    p = c.split()
    num = []
    for i in p:
        num.append(int(i))
        
    #State of the program after the  for loop has been executed: Output State: `n`, `x`, and `y` are integers such that 1 <= n, x, y <= 104 and x <= n; `num` contains the appended integer values from all elements in `p`; `p` is a non-empty iterable object.
    y = float(num[0] * num[2]) / float(100) - num[1]
    if (y % 1 == 0) :
        print(int(y))
    else :
        print(int(y) + 1)
    #State of the program after the if-else block has been executed: *`n`, `x`, and `y` are integers such that 1 <= n, x, y <= 104 and x <= n; `num` contains the appended integer values from all elements in `p`. If y is divisible by 1, the value of `y` is printed as an integer. Otherwise, the program continues with the same state of variables.
#Overall this is what the function does:The function `func` reads input values, calculates a specific formula, and determines whether the result is an integer or requires rounding up to the next integer. It does not accept any parameters. The calculation involves multiplying the first and third elements of the input, dividing by 100, subtracting the second element, and then determining whether the result should be rounded up to the next integer. The function outputs either the integer value of the result or that value plus 1.

