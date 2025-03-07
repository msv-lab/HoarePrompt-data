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
    (n, k) = func_3()
    v = 1
    for i in range(n, 0, -1):
        print(f'? 1 {i * n}', flush=True)
        v = func_2()
        if v == n:
            v = i
            break
    for i in range(1, n // k + 1):
        (cnt, l) = (k, 1)
        while cnt and l < n + 1:
            print(f'? {l} {i * v}', flush=True)
            l = func_2() + 1
            cnt -= 1
        if cnt == 0 and l == n + 1:
            print(f'! {i * v}', flush=True)
            func_2()
            return
    print('! -1', flush=True)
    func_2()
    return
for _ in range(int(input())):
    func_5()