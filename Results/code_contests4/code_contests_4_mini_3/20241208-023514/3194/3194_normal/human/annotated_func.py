#State of the program right berfore the function call: The input is a 3x3 matrix represented as a list of strings, where each string consists of three characters that are either 'X' or '.'
def func():
    lines = []
    for i in range(3):
        lines.append(sys.stdin.readline())
        
    #State of the program after the  for loop has been executed: `lines` contains three input lines, `i` is 3, and `lines` is a list with exactly three elements read from `sys.stdin`.
    if (lines[0][0] == 'X' and lines[2][2] != 'X' or lines[0][1] == 'X' and lines[
    2][1] != 'X' or lines[0][2] == 'X' and lines[2][0] != 'X' or lines[1][0
    ] == 'X' and lines[1][2] != 'X' or lines[1][2] == 'X' and lines[1][0] !=
    'X') :
        print('NO')
    else :
        print('YES')
    #State of the program after the if-else block has been executed: *`lines` contains three input lines, `i` is 3, and if the specified conditions are met, 'NO' is printed. Otherwise, 'YES' is printed.
#Overall this is what the function does:The function reads three lines of input representing a 3x3 matrix of characters ('X' or '.') and evaluates specific conditions based on the positions of 'X'. If any of the specified conditions involving 'X' are true, it prints 'NO'; otherwise, it prints 'YES'. The function does not return any value but prints the result directly. It assumes that the input is always a valid 3x3 matrix formatted as three strings of three characters each.

