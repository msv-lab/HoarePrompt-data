import math

def find_min_max_pair(X):
    min_max_value = X
    a, b = 1, X
    
    for d in range(1, int(math.sqrt(X)) + 1):
        if X % d == 0:
            e = X // d
            if max(d, e) < min_max_value:
                min_max_value = max(d, e)
                a, b = d, e
    
    return a, b

# Read input
X = int(input().strip())

# Find and print the result
a, b = find_min_max_pair(X)
print(a, b)
