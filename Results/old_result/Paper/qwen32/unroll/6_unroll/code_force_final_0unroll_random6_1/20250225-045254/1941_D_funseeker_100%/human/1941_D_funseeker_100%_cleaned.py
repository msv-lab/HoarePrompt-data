sys.setrecursionlimit(100000000)

def func_1():
    return sys.stdin.readline().strip()

def func_2():
    return int(func_1())

def func_3():
    return list(map(int, func_1().split()))
t = func_2()

def func_4():
    (n, m, x) = func_3()
    ans = {x}
    for _ in range(m):
        (r, c) = func_1().split()
        r = int(r)
        temp = set()
        for q in ans:
            if c == '0' or c == '?':
                temp.add((q + r) % n)
            if c == '1' or c == '?':
                temp.add((q - r) % n)
        ans = temp
    if 0 in ans:
        ans.discard(0)
        ans.add(n)
    print(len(ans))
    print(*sorted(ans))
for i in range(t):
    func_4()