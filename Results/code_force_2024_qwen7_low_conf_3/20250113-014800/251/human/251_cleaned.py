def func_1():
    import sys
    input = sys.stdin.read
    data = input().split()
    MOD = 1000000007
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        k = int(data[idx + 2])
        idx += 3
        (low, high) = (0, max(n, m) * 20)
        answer = high
        while low <= high:
            mid = (low + high) // 2
            if func_2(n, m, k, mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        p = answer
        q = 1
        q_inv = pow(q, MOD - 2, MOD)
        result = p * q_inv % MOD
        results.append(result)
    for res in results:
        print(res)

def func_2(n, m, k, steps):
    import math
    (h, w) = (n, m)
    for _ in range(steps):
        if h > w:
            h = max(h // 2, 1)
        else:
            w = max(w // 2, 1)
        if h * w < k:
            return True
    return h * w < k
if __name__ == '__main__':
    func_1()