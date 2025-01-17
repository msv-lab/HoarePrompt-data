from collections import deque

def can_reach_bottom_right(n, grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False] * n for _ in range(2)]
    queue = deque([(0, 0)])
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        
        if x == 1 and y == n - 1:
            return True
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 2 and 0 <= ny < n and not visited[nx][ny]:
                if grid[nx][ny] == '<' and dy == -1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif grid[nx][ny] == '>' and dy == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif (dx == 1 and dy == 0) or (dx == -1 and dy == 0):
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    return False

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        grid = [input().strip(), input().strip()]
        
        if can_reach_bottom_right(n, grid):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()