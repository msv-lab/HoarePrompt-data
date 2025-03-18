def func_1():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        v = [0] * (n + 1)
        for _ in range(n):
            x = int(data[idx])
            idx += 1
            v[x] += 1
        cnt = 0
        ans = 0
        for i in range(n + 1):
            if v[i] >= 2:
                ans += cnt * v[i] * (v[i] - 1) // 2
            if v[i] >= 3:
                ans += v[i] * (v[i] - 1) * (v[i] - 2) // 6
            cnt += v[i]
        results.append(str(ans))
    print('\n'.join(results))
if __name__ == '__main__':
    func_1()