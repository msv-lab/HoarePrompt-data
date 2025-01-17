def min_folded_length(test_cases):
    results = []
    for n, s in test_cases:
        max_segment_length = 1
        current_segment_length = 1
        
        for i in range(1, n):
            if s[i] == s[i - 1]:
                current_segment_length += 1
            else:
                max_segment_length = max(max_segment_length, current_segment_length)
                current_segment_length = 1
        
        # Check the last segment
        max_segment_length = max(max_segment_length, current_segment_length)
        
        results.append(max_segment_length)
    
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
results = min_folded_length(test_cases)

# Print results
for result in results:
    print(result)