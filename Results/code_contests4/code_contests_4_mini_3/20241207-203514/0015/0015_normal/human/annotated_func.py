#State of the program right berfore the function call: n, x, and y are integers such that 1 ≤ n, x, y ≤ 10^4 and x ≤ n.
def func():
    c = raw_input()
    p = c.split()
    num = []
    for i in p:
        num.append(int(i))
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 10^4, `x` is an integer such that 1 ≤ `x` ≤ `n`, `y` is an integer such that 1 ≤ `y` ≤ 10^4, `c` is a non-empty string, `p` is a list of substrings obtained by splitting `c`, `num` contains the integer values of all elements in `p`.
    y = float(num[0] * num[2]) / float(100) - num[1]
    if (y % 1 == 0) :
        print(int(y))
    else :
        print(int(y) + 1)
    #State of the program after the if-else block has been executed: *`n` is an integer such that 1 ≤ `n` ≤ 10^4, `x` is an integer such that 1 ≤ `x` ≤ `n`, and `y` is updated to (float(num[0] * num[2]) / float(100)) - num[1]. If `y` is an integer, the value of `y` is printed as an integer. Otherwise, the output is `int(y) + 1`, which is a specific integer value greater than `int(y)`.
#Overall this is what the function does:The function reads a line of input containing three integers, where the first integer (num[0]) corresponds to `n`, the second (num[1]) corresponds to `x`, and the third (num[2]) corresponds to `y`. It calculates the value of `y` as `(num[0] * num[2]) / 100 - num[1]`. If the calculated `y` is an integer, it prints that integer; if not, it prints the next higher integer. The function does not accept parameters directly and relies on user input. It does not handle cases where the input does not contain exactly three integers or where the integers are out of the specified bounds.

