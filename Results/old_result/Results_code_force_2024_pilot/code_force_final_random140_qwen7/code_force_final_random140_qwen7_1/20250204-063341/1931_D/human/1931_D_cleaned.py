def func_1(t, test_cases):
    results = []
    for case in test_cases:
        (n, x, y) = case['params']
        a = case['array']
        freq = defaultdict(int)
        beautiful_count = 0
        for num in a:
            mod_x = num % x
            mod_y = num % y
            required_mod_x = (x - mod_x) % x
            required_mod_y = mod_y
            if (required_mod_x, required_mod_y) in freq:
                beautiful_count += freq[required_mod_x, required_mod_y]
            freq[mod_x, mod_y] += 1
        results.append(beautiful_count)
    return results
t = int(input())
test_cases = []
for _ in range(t):
    (n, x, y) = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append({'params': (n, x, y), 'array': a})
results = func_1(t, test_cases)
for result in results:
    print(result)