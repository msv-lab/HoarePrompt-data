def func_1(board):
    lines = []
    for row in board:
        lines.append(row)
    for col in range(4):
        lines.append([board[row][col] for row in range(4)])
    lines.append([board[i][i] for i in range(4)])
    lines.append([board[i][3 - i] for i in range(4)])
    for line in lines:
        if line.count('x') == 2 and line.count('.') == 2:
            for i in range(3):
                if line[i:i + 3].count('x') == 2 and line[i:i + 3].count('.') == 1:
                    return 'YES'
    return 'NO'
board = []
for _ in range(4):
    board.append(list(input().strip()))
print(func_1(board))