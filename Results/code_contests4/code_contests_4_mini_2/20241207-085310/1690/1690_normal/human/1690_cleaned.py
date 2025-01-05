rstr = lambda : stdin.readline().strip()
rints = lambda : [int(x) for x in stdin.readline().split()]
(n, s, a, ans, word) = (int(input()), rstr(), rints(), float('inf'), 'hard')
for i in range(4):
    (be, en, tem) = (0, n, 0)
    cur = 0
    for j in range(n):
        if cur == i:
            break
        elif s[j] == word[cur]:
            cur += 1
        be += 1
    cur = 3
    for j in range(n - 1, -1, -1):
        if cur == i:
            break
        elif s[j] == word[cur]:
            cur -= 1
        en -= 1
    for j in range(be, en):
        if s[j] == word[i]:
            tem += a[j]
    ans = min(ans, tem)
print(ans)