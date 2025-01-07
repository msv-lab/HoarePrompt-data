(n, k) = map(int, input().split())
line = input()
G_pos = line.index('G')
T_pos = line.index('T')
if G_pos > T_pos:
    (G_pos, T_pos) = (T_pos, G_pos)
reachable = False
for pos in range(G_pos, T_pos + 1, k):
    if line[pos] == '#':
        break
    if pos == T_pos:
        reachable = True
        break
if reachable:
    print('YES')
else:
    print('NO')