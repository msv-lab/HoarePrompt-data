#State of the program right berfore the function call: n, x, and y are positive integers such that 1 <= n, x, y <= 10^4 and x <= n.**
def func():
    c = raw_input()
    p = c.split()
    num = []
    for i in p:
        num.append(int(i))
        
    #State of the program after the  for loop has been executed: Error: raw_input() is not a valid function in Python 3, `n`, `x`, and `y` remain unchanged, `num` is a list containing the integer values appended through the loop, for the loop to execute `p` must still have elements to iterate over
    y = float(num[0] * num[2]) / float(100) - num[1]
    if (y % 1 == 0) :
        print(int(y))
    else :
        print(int(y) + 1)
    #State of the program after the if-else block has been executed: *Error: raw_input() is not a valid function in Python 3, `n`, `x`, and `y` remain unchanged, `num` is a list containing the integer values appended through the loop, for the loop to execute `p` must still have elements to iterate over. If `y` is an integer and divisible by 1, the program continues as described. Otherwise, if `y` is not an integer, the program continues as described.
#Overall this is what the function does:The function `func` reads input values, performs a calculation, and then prints the result rounded up to the nearest integer. However, the annotation mentions divisibility cases related to `n`, `x`, and `y`, which are not implemented in the code. The actual functionality of the code is to take input values, perform a specific calculation, and print the rounded result.

