#State of the program right berfore the function call: The input is a 3x3 matrix represented as a list of strings, where each string consists of three characters that are either 'X' (pressed button) or '.' (not pressed button).
def func():
    lines = []
    for i in range(3):
        lines.append(sys.stdin.readline())
        
    #State of the program after the  for loop has been executed: `lines` contains three lines of input, `i` is 3.
    if (lines[0][0] == 'X' and lines[2][2] != 'X' or lines[0][1] == 'X' and lines[
    2][1] != 'X' or lines[0][2] == 'X' and lines[2][0] != 'X' or lines[1][0
    ] == 'X' and lines[1][2] != 'X' or lines[1][2] == 'X' and lines[1][0] !=
    'X') :
        print('NO')
    else :
        print('YES')
    #State of the program after the if-else block has been executed: *`lines` contains three lines of input, `i` is 3. If any of the specified conditions regarding 'X' in the lines are met, the output is 'NO'. Otherwise, if none of the conditions are met, "YES" is printed.
#Overall this is what the function does:The function reads three lines of input representing a 3x3 matrix of characters ('X' for pressed buttons and '.' for not pressed buttons). It checks specific conditions regarding the presence of 'X' in these lines. If any of the conditions are met, it prints 'NO'; otherwise, it prints 'YES'. The function does not accept any parameters and does not return a value. Potential edge cases include the possibility of receiving invalid input that does not conform to the expected 3x3 matrix format, which could lead to unexpected behavior.

