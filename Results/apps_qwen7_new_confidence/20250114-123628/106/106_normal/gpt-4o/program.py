from collections import deque, defaultdict

# Helper functions to generate valid moves for each piece
def knight_moves(x, y, N):
    moves = [
        (x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1),
        (x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2)
    ]
    return [(nx, ny) for nx, ny in moves if 0 <= nx < N and 0 <= ny < N]

def rook_moves(x, y, N):
    moves = []
    for i in range(N):
        if i != x:
            moves.append((i, y))
        if i != y:
            moves.append((x, i))
    return moves

def bishop_moves(x, y, N):
    moves = []
    for i in range(1, N):
        if 0 <= x+i < N and 0 <= y+i < N:
            moves.append((x+i, y+i))
        if 0 <= x+i < N and 0 <= y-i < N:
            moves.append((x+i, y-i))
        if 0 <= x-i < N and 0 <= y+i < N:
            moves.append((x-i, y+i))
        if 0 <= x-i < N and 0 <= y-i < N:
            moves.append((x-i, y-i))
    return moves

def bfs_min_steps(N, board):
    target_position = {}
    for i in range(N):
        for j in range(N):
            target_position[board[i][j]] = (i, j)
    
    # BFS queue: (steps, replacements, piece, x, y, current number)
    # piece: 0 for knight, 1 for rook, 2 for bishop
    queue = deque([(0, 0, 0, *target_position[1], 1), (0, 0, 1, *target_position[1], 1), (0, 0, 2, *target_position[1], 1)])
    visited = defaultdict(lambda: float('inf'))  # (x, y, piece, current number) -> (steps, replacements)
    
    while queue:
        steps, replacements, piece, x, y, current = queue.popleft()
        
        if current == N * N:
            return steps, replacements
        
        if (x, y, piece, current) in visited and visited[(x, y, piece, current)] <= (steps, replacements):
            continue
        
        visited[(x, y, piece, current)] = (steps, replacements)
        
        # Add moves for current piece
        if piece == 0:
            moves = knight_moves(x, y, N)
        elif piece == 1:
            moves = rook_moves(x, y, N)
        else:
            moves = bishop_moves(x, y, N)
        
        for nx, ny in moves:
            if board[nx][ny] == current + 1:
                queue.append((steps + 1, replacements, piece, nx, ny, current + 1))
            else:
                queue.append((steps + 1, replacements, piece, nx, ny, current))
        
        # Add piece replacements
        for new_piece in range(3):
            if new_piece != piece:
                queue.append((steps + 1, replacements + 1, new_piece, x, y, current))
    
    return -1, -1  # In case there is no valid path, which shouldn't happen

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    board = []
    index = 1
    for i in range(N):
        row = []
        for j in range(N):
            row.append(int(data[index]))
            index += 1
        board.append(row)
    
    steps, replacements = bfs_min_steps(N, board)
    print(steps, replacements)
