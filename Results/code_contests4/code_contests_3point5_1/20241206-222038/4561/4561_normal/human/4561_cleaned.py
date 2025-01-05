def func_1(n):
    prim[1] = 1
    for i in range(2, n):
        if not prim[i]:
            for j in range(i, n, i):
                prim[j] = i

def func_2(x):
    fac = []
    while x > 1:
        div = prim[x]
        fac.append(div)
        while x % div == 0:
            x //= div
    return fac
(Max, out) = (100001, [])
rstrs = lambda : [str(x) for x in stdin.readline().split()]
rints = lambda : [int(x) for x in stdin.readline().split()]
(prim, mem) = ([0] * Max, [set() for _ in range(Max)])
func_1(Max)
(n, m) = rints()
for _ in range(m):
    (sign, num) = rstrs()
    num = int(num)
    facs = func_2(num)
    if sign == '-':
        if num == 1:
            out.append('Already off' if not mem[1] else 'Success')
            mem[1].discard(1)
        else:
            ans = 'Already off'
            for i in facs:
                if num in mem[i]:
                    mem[i].discard(num)
                    ans = 'Success'
            out.append(ans)
    elif num == 1:
        out.append('Already on' if mem[1] else 'Success')
        mem[1].add(1)
    else:
        ans = 'Success'
        for i in facs:
            if num not in mem[i]:
                mem[i].add(num)
            elif ans == 'Success':
                ans = 'Already on'
            if len(mem[i]) > 1:
                mem[i].discard(num)
                j = mem[i].pop()
                ans = 'Conflict with %d' % j
                mem[i].add(j)
                break
        if ans[0] == 'C':
            for i in facs:
                mem[i].discard(num)
        out.append(ans)
print('\n'.join(map(str, out)))