input = sys.stdin.readline

def func_1():
    return list(map(int, input().split()))

def func_2():
    return int(input())

def func_3():
    return map(int, input().split())

def func_4():
    return input().strip()

def func_5():
    (n, x) = func_3()
    a = func_1()
    (t, ans) = ([], -1)
    for i in range(29, -1, -1):
        (u, v) = (x >> i & 1, sum([val >> i & 1 for val in a]))
        if u == v == 0:
            continue
        if u == 0:
            if v % 2:
                return ans
            else:
                op = ai = 0
                for val in a:
                    op ^= val >> i & 1
                    ai ^= val
                    if not op:
                        t.append(ai)
                        ai = 0
                (a, t) = (t, [])
        elif v % 2:
            continue
        elif v:
            op = cnt = 0
            for val in a:
                op ^= val >> i & 1
                if not op:
                    cnt += 1
            ans = max(ans, cnt)
        else:
            break
    return max(ans, len(a))
for _ in range(int(input())):
    print(func_5())