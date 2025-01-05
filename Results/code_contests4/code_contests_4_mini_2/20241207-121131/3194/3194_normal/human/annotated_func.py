#State of the program right berfore the function call: The input matrix is a 3x3 list of strings where each string consists of characters 'X' or '.', and there are no restrictions on the presence of 'X' or '.'.
def func():
    lines = []
    for i in range(3):
        lines.append(sys.stdin.readline())
        
    #State of the program after the  for loop has been executed: `lines` contains three input lines from `sys.stdin`, `i` is 2.
    if (lines[0][0] == 'X' and lines[2][2] != 'X' or lines[0][1] == 'X' and lines[
    2][1] != 'X' or lines[0][2] == 'X' and lines[2][0] != 'X' or lines[1][0
    ] == 'X' and lines[1][2] != 'X' or lines[1][2] == 'X' and lines[1][0] !=
    'X') :
        print('NO')
    else :
        print('YES')
    #State of the program after the if-else block has been executed: *`lines` contains three input lines from `sys.stdin`, and `i` is 2. If any of the specified conditions involving the 'X' character are met, 'NO' is printed. Otherwise, 'YES' is printed.
#Overall this is what the function does:The function reads three lines of input from standard input, each containing a string of characters 'X' or '.'. It then checks specific conditions involving the presence of 'X' in certain positions of the first and last lines, as well as the second line. If any of the conditions are met, it prints 'NO'; otherwise, it prints 'YES'. The function does not return any value but prints the result directly. It does not validate the input format or size beyond reading three lines.

