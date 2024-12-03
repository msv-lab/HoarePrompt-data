def can_win(board):
    # Check all possible lines
    lines = []

    # Rows
    for row in board:
        lines.append(row)

    # Columns
    for col in range(4):
        lines.append([board[row][col] for row in range(4)])

    # Diagonals
    lines.append([board[i][i] for i in range(4)])
    lines.append([board[i][3 - i] for i in range(4)])

    for line in lines:
        if line.count('x') == 2 and line.count('.') == 2:
            # Check all possible 3-in-a-row combinations within the 4-length line
            for i in range(3):
                if line[i:i+3].count('x') == 2 and line[i:i+3].count('.') == 1:
                    return "YES"
    
    return "NO"

# Read the board from standard input
board = []
for _ in range(4):
    board.append(list(input().strip()))

print(can_win(board))
