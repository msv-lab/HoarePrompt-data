def func_1(n, a):
    from collections import Counter
    counter = Counter(a)
    pairs = sum((1 for count in counter.values() if count == 2))
    return min(pairs, n // 2)

def func_2():
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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        results.append(func_1(n, a))
    for result in results:
        print(result)