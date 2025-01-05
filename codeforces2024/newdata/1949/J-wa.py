from collections import deque

def is_valid_move(grid, r, c, visited, i1, j1, i2, j2):
    # Check if the move is valid
    if i2 < 0 or i2 >= r or j2 < 0 or j2 >= c:
        return False
    if grid[i2][j2] == '*' or visited[i2][j2]:
        return False
    # Check if the move keeps the body connected
    connected_pixels = 0
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = i2 + di, j2 + dj
        if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == '*':
            connected_pixels += 1
    if connected_pixels < 2:
        return False
    return True

def bfs(grid, r, c, initial_position, final_position):
    # Initialize visited array
    visited = [[False] * c for _ in range(r)]
    # Initialize queue for BFS
    q = deque()
    # Add initial position to the queue
    q.append(initial_position)
    # Mark initial position as visited
    visited[initial_position[0]][initial_position[1]] = True
    # Initialize parent array to track moves
    parent = {}

    while q:
        # Get the current position
        current_position = q.popleft()
        # If the current position is the final position, break
        if current_position == final_position:
            break
        i, j = current_position
        # Explore all possible moves
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if is_valid_move(grid, r, c, visited, i, j, ni, nj):
                # Mark the new position as visited
                visited[ni][nj] = True
                # Add the new position to the queue
                q.append((ni, nj))
                # Store the parent of the new position
                parent[(ni, nj)] = (i, j)
    
    # If final position is not reachable, return None
    if final_position not in parent:
        return None
    
    # Reconstruct the path
    moves = []
    current_position = final_position
    while current_position != initial_position:
        parent_position = parent[current_position]
        moves.append((parent_position[0]+1, parent_position[1]+1, current_position[0]+1, current_position[1]+1))
        current_position = parent_position
    moves.reverse()
    return moves

def main():
    # Read input
    r, c = map(int, input().split())
    initial_grid = [input() for _ in range(r)]
    input()  # Read empty line
    final_grid = [input() for _ in range(r)]

    # Find initial and final positions
    initial_position = None
    final_position = None
    for i in range(r):
        for j in range(c):
            if initial_grid[i][j] == '*':
                initial_position = (i, j)
            if final_grid[i][j] == '*':
                final_position = (i, j)
    
    # Find sequence of moves using BFS
    moves = bfs(initial_grid, r, c, initial_position, final_position)

    # Output result
    if moves:
        print("YES")
        print(len(moves))
        for move in moves:
            print(*move)
    else:
        print("NO")

if __name__ == "__main__":
    main()
