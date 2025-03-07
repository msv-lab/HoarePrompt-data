def decode_string(encoded):
    # Get unique characters and sort them to form 'r'
    r = ''.join(sorted(set(encoded)))
    # Create the mapping dictionary
    mapping = {r[i]: r[-(i+1)] for i in range(len(r))}
    # Decode the string using the mapping
    return ''.join(mapping[char] for char in encoded)
 
# Reading input
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
    b = data[index]
    index += 1
    results.append(decode_string(b))
 
# Output the results
print('\n'.join(results))