from sys import stdin

s, ans = stdin.readline().strip(), float('inf')
for i in range(0, 10 ** 6):
    cur, tem = i, 0
    for j in range(5, -1, -1):
        tem += (cur % 10) != int(s[j])
        cur //= 10

    if sum([int(x) for x in str(i)[:3]]) == sum([int(y) for y in str(i)[3:]]):
        ans = min(ans, tem)
print(ans)
