from collections import deque
h, w, k = map(int, raw_input().split())
A = [raw_input() for i in xrange(h)]
sx = sy = 0
for i in xrange(h):
    idx = A[i].find('S')
    if idx != -1:
        sx = idx; sy = i
        break

deq = deque()
deq.append((0, (sx, sy)))

used = set([(sx, sy)])
dd = [[-1, 0], [0, -1], [1, 0], [0, 1]]

while deq:
    cost, [x, y] = deq.popleft()
    for dx, dy in dd:
        nx = x + dx; ny = y + dy
        if 0 <= nx < w and 0 <= ny < h:
            nkey = (nx, ny)
            if A[ny][nx] != '#' and nkey not in used:
                used.add(nkey)
                if cost + 1 < k:
                    deq.append((0, nkey))
ans = 10**18
for x, y in used:
    dx = min(x, w-1-x)
    dy = min(y, h-1-y)
    ans = min(ans, min(dx, dy))
print (ans+k-1)/k + 1