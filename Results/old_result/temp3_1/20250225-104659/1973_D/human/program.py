import sys

func_4()

def func_1(l, x):
    print(f'? {l} {x}')
    sys.stdout.flush()
    ret = int(input())
    assert ret >= 0
    return ret

def func_2(m):
    print(f'! {m}')
    sys.stdout.flush()
    ret = int(input())
    assert ret == 1

def func_3():
    (n, k) = map(int, input().split())
    max_val = 0
    for i in range(n, 0, -1):
        r = func_1(1, i * n)
        if r <= n:
            assert r == n
            max_val = i
            break
    assert max_val > 0
    for i in range(n // k, 0, -1):
        m = i * max_val
        p = 0
        for j in range(1, k + 1):
            p = func_1(p + 1, m)
            if p >= n:
                break
        if p == n:
            func_2(m)
            return
    func_2(-1)

def func_4():
    t = int(input())
    for _ in range(t):
        func_3()

