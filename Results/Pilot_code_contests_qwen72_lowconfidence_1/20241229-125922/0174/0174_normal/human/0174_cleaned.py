rints = lambda : [int(x) for x in stdin.readline().split()]
out = []
(n, a) = (int(input()), rints())
(mem, cols, rows) = (defaultdict(deque), n, n)
mem2 = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    if a[i] == 1:
        out.append('%d %d' % (rows, i + 1))
        if rows < 1:
            print(-1)
            exit()
        rows -= 1
        mem[1].append([rows + 1, i + 1])
    elif a[i] == 2:
        if mem[1]:
            out.append('%d %d' % (mem[1][0][0], i + 1))
        else:
            print(-1)
            exit()
        mem[1].popleft()
        mem[2].append(i + 1)
    elif a[i] == 3:
        if mem[3]:
            out.append('%d %d' % (rows, i + 1))
            out.append('%d %d' % (rows, mem[3][0]))
            if rows < 1:
                print(-1)
                exit()
            rows -= 1
            mem[3].popleft()
        elif mem[2]:
            out.append('%d %d' % (rows, i + 1))
            out.append('%d %d' % (rows, mem[2][0]))
            if rows < 1:
                print(-1)
                exit()
            rows -= 1
            mem[2].popleft()
        elif mem[1]:
            out.append('%d %d' % (rows, i + 1))
            out.append('%d %d' % (rows, mem[1][0][1]))
            if rows < 1:
                print(-1)
                exit()
            rows -= 1
            mem[1].popleft()
        else:
            print(-1)
            exit()
        mem[3].append(i + 1)
print('%d\n%s' % (len(out), '\n'.join(out)))