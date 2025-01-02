(n, m) = map(int, raw_input().split())
red = []
blue = []
for i in range(n):
    row = raw_input()
    r = ['#']
    b = ['.']
    for j in range(1, m - 1):
        if row[j] == '#':
            r.append('#')
            b.append('#')
        elif i % 2 == 0:
            r.append('#')
            b.append('.')
        else:
            r.append('.')
            b.append('#')
    r.append('.')
    b.append('#')
    red.append(''.join(r))
    blue.append(''.join(b))
for r in red:
    print(r)
for b in blue:
    print(b)