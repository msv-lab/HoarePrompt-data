from sys import stdin

n, a = int(input()), [int(x) for x in stdin.readline().split()]
mem = [0] * 200002
for i in range(n):
    mem[a[i]] += 1

ma = mem.index(max(mem))
out, tem = [ma] * mem[ma], []

for i in range(1, 20):
    if mem[i] < 2 and tem:
        if mem[i] == 1:
            tem.append(i)

        su = sum([mem[j] for j in tem])
        if su > len(out):
            out = tem
            for j in tem[::-1]:
                out.extend([j] * (mem[j] - 1))

        if not mem[i]:
            tem = []
        else:
            tem = [tem[-1]]
    elif mem[i]:
        tem.append(i)

print('%d\n%s' % (len(out), ' '.join(map(str, out))))
