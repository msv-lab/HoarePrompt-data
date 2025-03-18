def func_1(t, cases):
    results = []
    sequence = [2 ** i for i in range(25)]
    for (n, k) in cases:
        results.append((25, sequence))
    return results
input = sys.stdin.read
data = input().split()
t = int(data[0])
cases = []
index = 1
for _ in range(t):
    n = int(data[index])
    k = int(data[index + 1])
    cases.append((n, k))
    index += 2
results = func_1(t, cases)
for result in results:
    print(result[0])
    print(' '.join(map(str, result[1])))