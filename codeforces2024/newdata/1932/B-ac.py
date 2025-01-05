def find_apocalypse_year(n, periods):
    current_year = 0
    for period in periods:
        # Find the next occurrence of the current sign
        if current_year % period == 0:
            current_year += period
        else:
            current_year = ((current_year // period) + 1) * period
    return current_year

# Input reading
t = int(input())  # Number of test cases
results = []

for _ in range(t):
    n = int(input())  # Number of signs
    periods = list(map(int, input().split()))  # Periodicities of the signs
    results.append(find_apocalypse_year(n, periods))

# Output results
for result in results:
    print(result)
