def func_1(test_cases):
    results = []
    for case in test_cases:
        (n, a) = case
        a.sort()
        median_index = (n - 1) // 2
        median_value = a[median_index]
        operations = 0
        while median_index < n and a[median_index] == median_value:
            median_index += 1
            operations += 1
        results.append(operations)
    return results
input = sys.stdin.read
data = input().split()
index = 0
t = int(data[index])
index += 1
test_cases = []
for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index + n]))
    index += n
    test_cases.append((n, a))
results = func_1(test_cases)
for result in results:
    print(result)