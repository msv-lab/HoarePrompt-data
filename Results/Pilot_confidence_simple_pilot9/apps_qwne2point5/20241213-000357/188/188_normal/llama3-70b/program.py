n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
c = 0
a1, a2 = -1, -1
for i in d:
    if d[i] == n//2:
        if c == 0:
            a1 = i
            c += 1
        else:
            a2 = i
            break
if a1 != -1 and a2 != -1:
    print("YES")
    print(a1, a2)
else:
    print("NO")