def check_win(board, x, y):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    
    for dx, dy in directions:
        count = 1  # Start with the placement at (x, y)
        for step in range(1, 5):
            nx, ny = x + step * dx, y + step * dy
            if 0 <= nx < 10 and 0 <= ny < 10 and board[nx][ny] == 'X':
                count += 1
            else:
                break
        
        for step in range(1, 5):
            nx, ny = x - step * dx, y - step * dy
            if 0 <= nx < 10 and 0 <= ny < 10 and board[nx][ny] == 'X':
                count += 1
            else:
                break
        
        if count >= 5:
            return True
    
    return False

def can_alice_win(board):
    for i in range(10):
        for j in range(10):
            if board[i][j] == '.':
                if check_win(board, i, j):
                    return "YES"
    return "NO"

# Reading input
board = []
for _ in range(10):
    board.append(input().strip())

# Checking if Alice can win
print(can_alice_win(board))
