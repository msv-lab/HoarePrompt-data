from math import gcd

def is_non_decreasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def can_remove_one_to_make_gcd_sequence_non_decreasing(a):
    n = len(a)
    
    # Compute the initial GCD sequence
    b = [gcd(a[i], a[i + 1]) for i in range(n - 1)]
    
    # Check if the initial GCD sequence is already non-decreasing
    if is_non_decreasing(b):
        return "YES"
    
    # Identify violations
    violations = []
    for i in range(len(b) - 1):
        if b[i] > b[i + 1]:
            violations.append(i)
    
    # If there are more than one violation, it's impossible to fix with one removal
    if len(violations) > 1:
        return "NO"
    
    # Simulate removals around the violation
    for i in violations:
        # Remove a[i]
        new_b1 = b[:i] + [gcd(a[i - 1], a[i + 1])] + b[i + 1:]
        if is_non_decreasing(new_b1):
            return "YES"
        
        # Remove a[i + 1]
        new_b2 = b[:i + 1] + [gcd(a[i], a[i + 2])] + b[i + 2:]
        if is_non_decreasing(new_b2):
            return "YES"
    
    return "NO"

# Read input
import sys
input = sys.stdin.read
data = input().split()

index = 0
t = int(data[index])
index += 1

results = []

for _ in range(t):
    n = int(data[index])
    index += 1
    a = list(map(int, data[index:index + n]))
    index += n
    
    result = can_remove_one_to_make_gcd_sequence_non_decreasing(a)
    results.append(result)

# Print results
for result in results:
    print(result)