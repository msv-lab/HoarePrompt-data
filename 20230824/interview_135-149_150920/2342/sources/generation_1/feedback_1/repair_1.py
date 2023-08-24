t = int(input())

def can_escape(maze, n, m, visited, row, col):
    if row < 0 or row >= n or col < 0 or col >= m:
        return False
    if maze[row][col] == '#':
        return False
    if visited[row][col]:
        return False

    visited[row][col] = True

    if maze[row][col] == 'B':
        return False

    if row == n-1 and col == m-1:
        return True

    if (can_escape(maze, n, m, visited, row-1, col) or
        can_escape(maze, n, m, visited, row+1, col) or
        can_escape(maze, n, m, visited, row, col-1) or
        can_escape(maze, n, m, visited, row, col+1)):
        return True

    return False

for _ in range(t):
    n, m = map(int, input().split())
    maze = [list(input()) for _ in range(n)]
    
    # Check if there are any good people or bad people in the maze
    has_good_people = False
    has_bad_people = False
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'G':
                has_good_people = True
            elif maze[i][j] == 'B':
                has_bad_people = True
    
    if not has_good_people:
        print("Yes")
        continue
    elif not has_bad_people:
        print("Yes")
        continue
    
    # Create a visited array to keep track of visited cells
    visited = [[False]*m for _ in range(n)]
    
    # Find all the good people in the maze and check if they can reach the destination cell
    possible = True
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'G':
                if not can_escape(maze, n, m, visited, i, j):
                    possible = False
                    break
    
    if possible:
        print("Yes")
    else:
        print("No")