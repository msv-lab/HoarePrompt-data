from sys import stdout
def main():
    n = int(raw_input())
    a = map(int, raw_input().split())
    d = [[] for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(i + 1, n):
            if a[i] > a[j]:
                d[i].append(j)
    ans = []
    for i in xrange(n):
        d[i].sort(key=lambda x: (-a[x], -x))
        for j in d[i]:
            ans.append((i + 1, j + 1))
            a[i], a[j] = a[j], a[i]
    stdout.write(str(len(ans)) + '\n')
    stdout.write(''.join("%d %d\n" % (x, y) for x, y in ans))
main()
