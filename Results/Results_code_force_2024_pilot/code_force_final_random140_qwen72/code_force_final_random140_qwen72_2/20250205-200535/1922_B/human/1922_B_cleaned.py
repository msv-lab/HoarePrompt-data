def func_1():
    import sys
    input = sys.stdin.read
    data = input().split()
    current_index = 0
    t = int(data[current_index])
    current_index += 1
    results = []
    for _ in range(t):
        hashing = {}
        n = int(data[current_index])
        current_index += 1
        a = []
        for i in range(n):
            a.append(int(data[current_index]))
            current_index += 1
        a.sort()
        ans = 0
        for i in range(n - 1):
            if a[i] not in hashing:
                hashing[a[i]] = 0
            hashing[a[i]] += i
            if a[i] == a[i + 1]:
                ans += hashing[a[i]]
        results.append(ans)
    for result in results:
        print(result)
func_1()