n, m = map(int, input().split())
field = [list(input()) for _ in range(n)]

def count_bombs(i, j):
    bombs = 0
    for x in range(max(0, i-1), min(n, i+2)):
        for y in range(max(0, j-1), min(m, j+2)):
            if (x, y) != (i, j) and field[x][y] == '*':
                bombs += 1
    return bombs

for i in range(n):
    for j in range(m):
        if field[i][j].isdigit():
            if int(field[i][j]) != count_bombs(i, j):
                print("NO")
                exit()
        elif field[i][j] == '.':
            if count_bombs(i, j) > 0:
                print("NO")
                exit()

print("YES")
