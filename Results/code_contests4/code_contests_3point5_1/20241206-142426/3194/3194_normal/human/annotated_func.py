#State of the program right berfore the function call: The input matrix is a 3x3 grid containing only the symbols 'X' and '.'.**
def func():
    lines = []
    for i in range(3):
        lines.append(sys.stdin.readline())
        
    #State of the program after the  for loop has been executed: The input matrix is a 3x3 grid containing only the symbols 'X' and '.', `lines` contains 5 lines with the last line read from standard input, `i` is 4 indicating the loop has completed all iterations
    if (lines[0][0] == 'X' and lines[2][2] != 'X' or lines[0][1] == 'X' and lines[
    2][1] != 'X' or lines[0][2] == 'X' and lines[2][0] != 'X' or lines[1][0
    ] == 'X' and lines[1][2] != 'X' or lines[1][2] == 'X' and lines[1][0] !=
    'X') :
        print('NO')
    else :
        print('YES')
    #State of the program after the if-else block has been executed: *The input matrix is a 3x3 grid containing only the symbols 'X' and '.', `lines` contains 5 lines with the last line read from standard input, `i` is 4 indicating the loop has completed all iterations. If the specified patterns of 'X' and its surroundings are found in the input matrix based on the conditions in the if statement, 'NO' is printed. Otherwise, if none of the specified patterns are found, 'YES' is printed.
#Overall this is what the function does:Functionality: The function `func` reads input lines to form a 3x3 grid matrix containing only 'X' and '.' symbols. It then checks specific patterns around 'X' positions in the matrix. If any of these patterns are found, it prints 'NO'; otherwise, it prints 'YES'. The function does not accept any parameters and does not return any specific output based on the input grid.

