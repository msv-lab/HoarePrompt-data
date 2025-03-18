(x, y) = map(int, input().split())
lst = defaultdict(list)
for _ in range(x - 1):
    (a, b) = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
s = True
while lst[x] != []:
    while lst[x]:
        y = lst[x].pop()
        if lst[y] != []:
            x = y
            break
    s = not s
s = not s
print('Hermione' if s else 'Ron')