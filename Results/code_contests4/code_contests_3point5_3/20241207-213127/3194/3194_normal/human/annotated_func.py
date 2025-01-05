#State of the program right berfore the function call: Input is a 3x3 matrix containing symbols 'X' and '.' only.**
def func():
    lines = []
    for i in range(3):
        lines.append(sys.stdin.readline())
        
    #State of the program after the  for loop has been executed: Input is a 4x3 matrix containing symbols 'X' and '.', `lines` contains the 4 rows of the matrix
    if (lines[0][0] == 'X' and lines[2][2] != 'X' or lines[0][1] == 'X' and lines[
    2][1] != 'X' or lines[0][2] == 'X' and lines[2][0] != 'X' or lines[1][0
    ] == 'X' and lines[1][2] != 'X' or lines[1][2] == 'X' and lines[1][0] !=
    'X') :
        print('NO')
    else :
        print('YES')
    #State of the program after the if-else block has been executed: *Input is a 4x3 matrix containing symbols 'X' and '.', `lines` contains the 4 rows of the matrix. If any of the specified conditions in the if statement are satisfied, the program will have certain cells containing 'X', otherwise, the cells will not have 'X' based on the specified conditions.
#Overall this is what the function does:The function `func` reads input for a 3x3 matrix containing symbols 'X' and '.' only. It then checks specific positions in the matrix to determine if certain conditions are met. If any of these conditions are satisfied, it prints 'NO'; otherwise, it prints 'YES'. The function does not accept any parameters explicitly, and the output is directly printed to the console.

