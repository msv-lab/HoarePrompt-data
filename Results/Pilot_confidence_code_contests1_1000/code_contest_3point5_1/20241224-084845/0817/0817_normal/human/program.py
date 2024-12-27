from sys import stdin

rstr = lambda: stdin.readline().strip()
n, s = int(input()), rstr()
lst, ans = ['a'] * 26, [1] * n

for i in range(n):
    for j in range(26):
        if s[i] >= lst[j]:
            lst[j] = s[i]
            ans[i] = j + 1
            break

print('%d\n%s' % (max(ans), ' '.join(map(str, ans))))
