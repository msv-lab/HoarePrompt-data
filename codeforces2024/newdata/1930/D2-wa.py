def sum_of_f_over_substrings(t, test_cases):
    results = []
    
    for n, s in test_cases:
        total_sum = 0
        # Iterate over each starting position of the substring
        for i in range(n):
            count_ones = 0
            # Extend the substring from position i to j
            for j in range(i, n):
                if s[j] == '1':
                    count_ones += 1
                # Add the number of 1s in the current substring to the total sum
                total_sum += count_ones
        
        results.append(total_sum)
    
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
results = sum_of_f_over_substrings(t, test_cases)

# Print results
for result in results:
    print(result)