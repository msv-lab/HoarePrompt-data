def apocalypse(t, test_cases):
    results = []
    for test in test_cases:
        n, a = test
        current_year = 0
        for ai in a:
            # Find the next year when the sign ai occurs
            if current_year % ai == 0:
                next_year = current_year + ai
            else:
                next_year = ((current_year // ai) + 1) * ai
            current_year = next_year
        results.append(current_year)
    return results
 
# Read input
t = int(input().strip())
test_cases = []
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    test_cases.append((n, a))
 
# Get results
results = apocalypse(t, test_cases)
 
# Print results
for result in results:
    print(result)