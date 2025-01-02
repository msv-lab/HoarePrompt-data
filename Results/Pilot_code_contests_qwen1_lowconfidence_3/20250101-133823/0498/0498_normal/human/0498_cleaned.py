rints = lambda : [int(x) for x in stdin.readline().split()]

def func_1():
    (mem, mem2, out) = (Counter(w), defaultdict(list), [])
    for (x, y) in a:
        mem2[y - x].append([x, y])
    for (i, j) in mem.items():
        if len(mem2[i]) != j:
            print('NO')
            exit()
        mem2[i].sort(reverse=True)
    for i in range(n):
        (x, y) = mem2[w[i]][-1]
        labels[x][y] = i + 1
        if i and labels[x + 1][y] < labels[x][y] or labels[x][y + 1] < labels[x][y]:
            print('NO')
            exit()
        out.append(' '.join(map(str, mem2[w[i]].pop())))
    print('YES')
    print('\n'.join(out))
(n, labels) = (int(input()), [[0 for _ in range(1000)] for _ in range(1000)])
(a, w) = ([rints() for _ in range(n)], rints())
func_1()