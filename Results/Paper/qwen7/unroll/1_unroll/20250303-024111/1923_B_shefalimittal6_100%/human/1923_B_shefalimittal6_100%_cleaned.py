def func_1(a, x, k):
    n = len(a)
    sorted_indices = sorted(range(n), key=lambda i: abs(x[i]))
    distance = 0
    pos = 0
    while pos != len(sorted_indices):
        if abs(x[sorted_indices[pos]]) == distance:
            return False
        rest = k
        while rest != 0 and pos != len(sorted_indices):
            delta = min(rest, a[sorted_indices[pos]])
            rest -= delta
            a[sorted_indices[pos]] -= delta
            if a[sorted_indices[pos]] == 0:
                pos += 1
        distance += 1
    return True

def func_2():
    t = int(input())
    for _ in range(t):
        (n, k) = map(int, input().split())
        a = list(map(int, input().split()))
        x = list(map(int, input().split()))
        print('YES' if func_1(a, x, k) else 'NO')
if __name__ == '__main__':
    func_2()