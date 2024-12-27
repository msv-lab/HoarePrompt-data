from sys import stdin, stdout

t = input()
inp = stdin.readlines()
out = []

for itr in xrange(t):
    n = int(inp[itr << 1].strip())
    a = map(int, inp[itr << 1 | 1].strip().split())

    flag = 0
    for i in xrange(n - 1):
        if abs(a[i] - a[i + 1]) >= 2:
            out.append("YES")
            out.append(' '.join([str(i + 1), str(i + 2)]))
            flag = 1
            break

    if flag == 0:
        out.append("NO")

stdout.write("\n".join(out))