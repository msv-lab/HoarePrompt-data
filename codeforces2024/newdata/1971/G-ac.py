import sys

input = lambda: sys.stdin.readline().strip()
write = sys.stdout.write

t = int(input())
res = [0] * t

def to_hashable(x):
	return -x * 4

for ti in range(t):
    n = int(input())
    la = list(map(int, input().split()))

    save = {}
    for i in la:
        var_i = to_hashable(i // 4)
        if var_i not in save:
            save[var_i] = []
        save[var_i].append(i)

    for i in save:
        save[i].sort(reverse = True)

    ans = [save[to_hashable(i // 4)].pop() for i in la]
    res[ti] = ans

write('\n'.join(map(lambda t: ' '.join(map(str, t)), res)))
    