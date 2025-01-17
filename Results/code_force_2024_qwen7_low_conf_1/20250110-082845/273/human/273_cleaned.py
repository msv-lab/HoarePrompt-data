def func_1():
    n = int(input())
    a = list(map(int, input().split()))
    positions = []
    for i in range(n):
        positions.append((i + 1, i + 1))
    visit = [-1] * n
    for i in range(n):
        found = False
        for j in range(n):
            if i != j:
                dist = abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1])
                if dist == a[i]:
                    visit[i] = j + 1
                    found = True
                    break
        if not found:
            print('NO')
            return
    print('YES')
    for pos in positions:
        print(pos[0], pos[1])
    print(' '.join(map(str, visit)))
func_1()