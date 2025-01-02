from sys import stdin

rint = lambda: int(stdin.readline())
rints = lambda: [int(x) for x in stdin.readline().split()]
out = []
for _ in range(int(input())):
    n, a = rint(), rints()
    ans, mem = ['0'] * n, [0] * (n + 1)
    ans[0], l, r = '1', 0, n - 1

    for i in range(n):
        mem[a[i]] += 1
        if mem[a[i]] == 2:
            ans[0] = '0'

    for i in range(1, n):
        if not mem[i]:
            break
        ans[n - i] = '1'

        if a[l] != i and a[r] != i or a[l] == a[r] == i:
            break
        elif a[l] == i:
            l += 1
        else:
            r -= 1

    out.append(''.join(ans))

print('\n'.join(out))
