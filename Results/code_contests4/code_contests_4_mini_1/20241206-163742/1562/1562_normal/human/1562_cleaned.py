def func_1(y, x):
    if 0 <= y <= 11 and 0 <= x <= 11:
        return True
    return False

def func_2(y, x):
    if g[y][x] == '0':
        return 0
    g[y][x] = '0'
    for i in xrange(4):
        nexty = y + dy[i]
        nextx = x + dx[i]
        if not func_1(nexty, nextx):
            continue
        if visited[nexty][nextx] == 0 and g[nexty][nextx] == '1':
            visited[nexty][nextx] = 1
            func_2(nexty, nextx)
    return 1
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
while 1:
    try:
        g = [[] for _ in xrange(12)]
        for i in xrange(12):
            for j in raw_input():
                g[i].append(j)
        cnt = 0
        visited = [[0] * 12 for _ in xrange(12)]
        for i in xrange(12):
            for j in xrange(12):
                cnt += func_2(i, j)
        print(cnt)
        raw_input()
    except:
        break