n, m = map(int, input().split())
field = [input() for _ in range(n)]
walls = [(i, j) for i in range(n) for j in range(m) if field[i][j] == '*']

def can_wipe_out(x, y):
    for i in range(n):
        if all(field[i][j] == '.' for j in range(m) if j != y):
            return False
    for j in range(m):
        if all(field[i][j] == '.' for i in range(n) if i != x):
            return False
    return True

for x, y in walls:
    if can_wipe_out(x, y):
        print("YES")
        print(x + 1, y + 1)
        exit()
print("NO")
