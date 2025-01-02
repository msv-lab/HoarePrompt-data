(n, q) = map(int, stdin.readline().split())
queue = deque()
cnt = 0

def func_1(l, r):
    if r != l:
        ind = (r + l) // 2
        func_1(l, ind)
        func_1(ind + 1, r)
        func_2(l, ind, ind + 1, r)

def func_2(lf, rf, ls, rs):
    a = []
    ind1 = lf
    ind2 = ls
    while ind1 <= rf and ind2 <= rs:
        if queue[ind1] < queue[ind2]:
            a.append(queue[ind1])
            ind1 += 1
        else:
            a.append(queue[ind2])
            ind2 += 1
    while ind1 <= rf:
        a.append(queue[ind1])
        ind1 += 1
    while ind2 <= rs:
        a.append(queue[ind2])
        ind2 += 1
    for i in range(lf, rs + 1):
        queue[i] = a[i - lf]
used = [0 for i in range(n + 1)]
label = 1
for i in range(q):
    s = set()
    (tc, k, tp) = map(int, stdin.readline().split())
    if queue:
        func_1(0, len(queue) - 1)
    while queue and tc >= queue[0][0]:
        s.add(queue[0][2])
        cnt -= queue[0][1]
        queue.popleft()
    for i in range(1, n + 1):
        if used[i] in s:
            used[i] = 0
    if cnt + k <= n:
        ans = 0
        value = 0
        for i in range(1, n + 1):
            if not used[i]:
                ans += i
                value += 1
                used[i] = label
            if value == k:
                break
        stdout.write(str(ans) + '\n')
        cnt += k
        queue.append((tc + tp, k, label))
        label += 1
    else:
        stdout.write('-1\n')