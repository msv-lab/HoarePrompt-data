t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    maze = [list(input()) for _ in range(n)]
    
    possible = True
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'G':
                # Check if there is a bad person nearby
                if i < n-1 and maze[i+1][j] == 'B':
                    possible = False
                    break
                elif i > 0 and maze[i-1][j] == 'B':
                    possible = False
                    break
                elif j < m-1 and maze[i][j+1] == 'B':
                    possible = False
                    break
                elif j > 0 and maze[i][j-1] == 'B':
                    possible = False
                    break
            elif maze[i][j] == 'B':
                # Check if there is a good person nearby
                if i < n-1 and maze[i+1][j] == 'G':
                    possible = False
                    break
                elif i > 0 and maze[i-1][j] == 'G':
                    possible = False
                    break
                elif j < m-1 and maze[i][j+1] == 'G':
                    possible = False
                    break
                elif j > 0 and maze[i][j-1] == 'G':
                    possible = False
                    break
    
    if possible:
        print("Yes")
    else:
        print("No")