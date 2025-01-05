#State of the program right berfore the function call: The input matrix is a 3x3 grid containing either 'X' or '.' symbols.**
def func():
    lines = []
    for i in range(3):
        lines.append(sys.stdin.readline())
        
    #State of the program after the  for loop has been executed: The input matrix is a 4x3 grid containing either 'X' or '.' symbols; `lines` contains multiple lines of input
    if (lines[0][0] == 'X' and lines[2][2] != 'X' or lines[0][1] == 'X' and lines[
    2][1] != 'X' or lines[0][2] == 'X' and lines[2][0] != 'X' or lines[1][0
    ] == 'X' and lines[1][2] != 'X' or lines[1][2] == 'X' and lines[1][0] !=
    'X') :
        print('NO')
    else :
        print('YES')
    #State of the program after the if-else block has been executed: *The input matrix is a 4x3 grid containing either 'X' or '.' symbols; `lines` contains multiple lines of input. If any of the specified conditions in the if statement are true, then the program prints 'NO'. Otherwise, if none of the specified conditions are met, the program prints 'YES'.
#Overall this is what the function does:The function `func` reads input from the user as a 3x3 grid containing either 'X' or '.' symbols. It then checks specific conditions within the grid and prints 'NO' if any of those conditions are met, otherwise it prints 'YES'. The function does not accept any parameters and does not return any value.

