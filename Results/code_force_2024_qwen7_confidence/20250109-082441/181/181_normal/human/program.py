def find_nearly_shortest_repeating_substring(t, test_cases):
    results = []
    for n, s in test_cases:
        for l in range(1, n + 1):
            # Create the repeated string c from the first l characters of s
            k = s[:l]
            c = (k * (n // l)) + k[:n % l]
            
            # Check if c differs from s in at most one position
            diff_count = sum(1 for i in range(n) if s[i] != c[i])
            
            if diff_count <= 1:
                results.append(l)
                break
    return results

# Read input
import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
test_cases = []
for _ in range(t):
    n = int(data[index])
    s = data[index + 1]
    test_cases.append((n, s))
    index += 2

# Get results
results = find_nearly_shortest_repeating_substring(t, test_cases)

# Print results
for result in results:
    print(result)