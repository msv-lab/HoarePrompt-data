def can_transform(s, t):
    i, j = 0, 0
    n, m = len(s), len(t)
    
    while i < n or j < m:
        # Skip over '-' in s
        while i < n and s[i] == '-':
            i += 1
        # Skip over '-' in t
        while j < m and t[j] == '-':
            j += 1
        
        # Check if we reached the end of either string
        if i == n or j == m:
            break
        
        # If both are '*', we can skip any number of characters
        if s[i] == '*' or t[j] == '*':
            return True
        
        # If characters don't match, return False
        if s[i] != t[j]:
            return False
        
        i += 1
        j += 1
    
    # Handle remaining '*' characters
    while i < n and s[i] == '*':
        i += 1
    while j < m and t[j] == '*':
        j += 1
    
    # If both pointers reach the end, return True
    return i == n and j == m

# Read input
import sys
input = sys.stdin.read
data = input().split()

n, m = int(data[0]), int(data[1])
s = data[2]
t = data[3]

# Solve the problem
result = "Yes" if can_transform(s, t) else "No"
print(result)