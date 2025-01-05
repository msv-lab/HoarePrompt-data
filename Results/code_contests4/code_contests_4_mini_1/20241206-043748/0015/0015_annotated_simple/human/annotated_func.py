#State of the program right berfore the function call: n, x, and y are integers such that 1 ≤ n, x, y ≤ 10^4, and x ≤ n.
def func():
    c = raw_input()
    p = c.split()
    num = []
    for i in p:
        num.append(int(i))
        
    #State of the program after the  for loop has been executed: `n` is an integer, `x` is an integer, `y` is an integer, `p` is a list of substrings, `num` is a list containing the integer values of all elements in `p`, `i` is the last element in `p` if `p` is not empty, otherwise `i` is undefined.
    y = float(num[0] * num[2]) / float(100) - num[1]
    if (y % 1 == 0) :
        print(int(y))
    else :
        print(int(y) + 1)
    #State of the program after the if-else block has been executed: *`n` and `x` are integers, `y` is the result of the calculation and if `y` is an integer, it is printed. Otherwise, an error occurs stating that `y` cannot be converted to an integer as it is not an integer.
#Overall this is what the function does:The function reads input from the user, which consists of three integers (n, x, y) separated by spaces. It calculates a value `y` based on the formula `(num[0] * num[2]) / 100 - num[1]`, where `num[0]`, `num[1]`, and `num[2]` correspond to the integers n, x, and y respectively. If the calculated value `y` is an integer, it prints that integer; otherwise, it prints the next higher integer. The function does not return any value, and it lacks parameter acceptance as it relies on user input directly. It also assumes that the input will always be valid integers within the specified constraints.

