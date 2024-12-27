from sys import stdin
from collections import Counter


def solve():
    be, en, ans, cur, most = -1, -1, float('inf'), 0, Counter(a).most_common(1)[0][0]

    for i in range(n):
        if a[i] == most:
            if be == -1:
                be = i
            else:
                ans = min(ans, i - be + 1)
                be = i

    return str(ans)


out = []
for i in range(int(stdin.readline())):
    n, a = int(stdin.readline()), list(map(int, stdin.readline().split()))
    out.append(str(-1) if n == 1 else solve())

print('\n'.join(out))
