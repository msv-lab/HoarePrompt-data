(n, k) = map(int, raw_input().split())
s = raw_input()
alpha = string.uppercase[:k]
ans1 = list(s)
ans2 = list(s)
(rec1, rec2) = (0, 0)
for i in range(0, len(s), 2):
    neigh = ()
    if i > 0:
        neigh += (s[i - 1],)
    if i < n - 1:
        neigh += (s[i + 1],)
    if i > 0 and s[i] == s[i - 1] or (i < n - 1 and s[i] == s[i + 1]):
        for c in alpha:
            if c not in neigh:
                chosen = c
                break
        else:
            break
        ans1[i] = chosen
        rec1 += 1
for i in range(1, len(s), 2):
    neigh = ()
    if i > 0:
        neigh += (s[i - 1],)
    if i < n - 1:
        neigh += (s[i + 1],)
    if i > 0 and s[i] == s[i - 1] or (i < n - 1 and s[i] == s[i + 1]):
        for c in alpha:
            if c not in neigh:
                chosen = c
                break
        else:
            break
        ans2[i] = chosen
        rec2 += 1
valid1 = True
for i in range(1, len(ans1)):
    if ans1[i] == ans1[i - 1]:
        valid1 = False
        break
valid2 = True
for i in range(1, len(ans2)):
    if ans2[i] == ans2[i - 1]:
        valid2 = False
        break
if rec1 < rec2 and valid1 or not valid2:
    print(rec1)
    print(''.join(ans1))
else:
    print(rec2)
    print(''.join(ans2))