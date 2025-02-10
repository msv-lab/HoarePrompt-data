def minimum_operations_to_increase_median(test_cases):
    results = []
    for case in test_cases:
        n, a = case
        a.sort()
        median_index = (n - 1) // 2
        median_value = a[median_index]
        
        operations = 0
        while median_index < n and a[median_index] == median_value:
            median_index += 1
            operations += 1
        
        results.append(operations)
    
    return results
 
# Read input
import sys
input = sys.stdin.read
data = input().split()
 
# Parse input
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
 
# Compute results
results = minimum_operations_to_increase_median(test_cases)
 
# Print results
for result in results:
    print(result)