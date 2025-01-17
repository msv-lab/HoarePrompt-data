def func_1(t, test_cases):
    results = []
    for case in test_cases:
        (n, x, a) = case
        prefix_xor = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_xor[i] = prefix_xor[i - 1] ^ a[i - 1]
        current_xor = 0
        segment_count = 0
        valid = False
        for i in range(1, n + 1):
            current_xor ^= a[i - 1]
            if current_xor | prefix_xor[n] <= x:
                segment_count += 1
                current_xor = 0
                valid = True
        if valid:
            results.append(segment_count)
        else:
            results.append(-1)
    return results
input = sys.stdin.read
data = input().split()
t = int(data[0])
index = 1
test_cases = []
for _ in range(t):
    n = int(data[index])
    x = int(data[index + 1])
    a = list(map(int, data[index + 2:index + 2 + n]))
    test_cases.append((n, x, a))
    index += 2 + n
results = func_1(t, test_cases)
for result in results:
    print(result)