board = [input() for _ in range(4)]

def check_win(player, x, y, dx, dy):
    count = 0
    for i in range(4):
        nx, ny = x + i * dx, y + i * dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            if board[nx][ny] == player:
                count += 1
            else:
                break
        else:
            break
    return count >= 3

def can_win():
    for i in range(4):
        for j in range(4):
            if board[i][j] == '.':
                board[i][j] = 'x'
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    if check_win('x', i, j, dx, dy):
                        return True
                board[i][j] = '.'
    return False

print("YES" if can_win() else "NO")
