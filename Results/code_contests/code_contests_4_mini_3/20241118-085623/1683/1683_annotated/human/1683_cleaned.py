n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split(' ')))
a = a[::-1]
ans = []
vis = set({})
for ai in a:
    if ai in vis:
        continue
    else:
        ans.append(ai)
        vis.add(ai)
print(len(ans))
print(' '.join(map(str, ans[::-1])))