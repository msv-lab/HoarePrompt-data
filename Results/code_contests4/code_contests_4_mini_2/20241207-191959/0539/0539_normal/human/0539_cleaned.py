(target, n) = map(int, raw_input().split())
A = []
s = 0
for i in range(1, n + 1):
    k = (i & -i) - 1
    if i != 1 and k == i - 1:
        k = int(math.log(i, 2))
    A.append((2 ** k, i))
    s += A[-1][0]
if s < target:
    print(-1)
    exit()
A.sort()
selected = []
for tup in A:
    target -= tup[0]
    selected.append(tup[1])
    if target <= 0:
        break
print(len(selected))
print(' '.join(map(str, selected)))