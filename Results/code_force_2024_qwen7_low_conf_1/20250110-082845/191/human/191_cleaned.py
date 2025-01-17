MOD = 10 ** 9 + 7

def func_1():
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        k = int(data[index + 1])
        index += 2
        rows = set()
        cols = set()
        for _ in range(k):
            r = int(data[index])
            c = int(data[index + 1])
            index += 2
            rows.add(r)
            cols.add(c)
            if r != c:
                rows.add(c)
                cols.add(r)
        free_rows = n - len(rows)
        free_cols = n - len(cols)
        m = min(free_rows, free_cols)
        result = 1
        for i in range(1, m + 1):
            result = result * i % MOD
        results.append(result)
    for res in results:
        print(res)