input = sys.stdin.readline
sys.setrecursionlimit(int(1000000000.0))

def func_1(a, b, c, d):
    print(f'? {a} {b} {c} {d}')
    sys.stdout.flush()
    return input().strip()

def func_2(a, b):
    print(f'! {a} {b}')
    sys.stdout.flush()

def func_3():
    n = int(input())
    if n == 2:
        func_2(0, 1)
        return
    max_index = 0
    for i in range(0, n):
        res = func_1(0, max_index, 0, i)
        if res == '<':
            max_index = i
    min_indices = [max_index]
    for i in range(0, n):
        res = func_1(max_index, min_indices[0], max_index, i)
        if res == '<':
            min_indices = [i]
        else:
            min_indices.append(i)
    min_index = min_indices[0]
    for i in min_indices:
        if i == max_index:
            continue
        res = func_1(min_index, min_index, min_index, i)
        if res == '=':
            min_index = i
    func_2(max_index, min_index)
T = int(input())
for _ in range(T):
    func_3()