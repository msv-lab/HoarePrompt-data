#State of the program right berfore the function call: n, x, and y are integers such that 1 ≤ n, x, y ≤ 104 and x ≤ n.**
def func():
    c = raw_input()
    p = c.split()
    num = []
    for i in p:
        num.append(int(i))
        
    #State of the program after the  for loop has been executed: `n`, `x`, `y` are integers such that 1 ≤ n, x, y ≤ 104 and x ≤ n; `p` has been fully iterated through, `num` is a list containing the integer values of all elements in `p`
    y = float(num[0] * num[2]) / float(100) - num[1]
    if (y % 1 == 0) :
        print(int(y))
    else :
        print(int(y) + 1)
    #State of the program after the if-else block has been executed: *n, x, y are integers such that 1 ≤ n, x, y ≤ 104 and x ≤ n; p has been fully iterated through, num is a list containing the integer values of all elements in p. If y is an integer multiple of 1, then the program stays the same. Otherwise, the value of y is incremented by 1.
#Overall this is what the function does:The function `func` reads input from the user, splits it into integers, calculates a value `y`, and prints the integer value of `y` or `y + 1` based on whether `y` is an integer multiple of 1. The function does not accept any parameters, and the specific purpose or context of this calculation is not explicitly defined in the provided information.

