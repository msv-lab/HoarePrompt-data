n, p, q = map(int, input().split())
s = input()

k = 0
pieces = []
while len(s) > 0:
    if len(s) >= p:
        pieces.append(s[:p])
        s = s[p:]
        k += 1
    elif len(s) >= q:
        pieces.append(s[:q])
        s = s[q:]
        k += 1
    else:
        break

if len(s) > 0:
    print(-1)
else:
    print(k)
    for piece in pieces:
        print(piece)
