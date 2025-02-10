def decode_string(encoded):
    # Determine the auxiliary string r
    unique_chars = sorted(set(encoded))
    r = ''.join(unique_chars)
 
    # Create the mapping from encoded characters to original characters
    char_map = {char: r[-i-1] for i, char in enumerate(r)}
 
    # Decode the string using the mapping
    decoded = ''.join(char_map[char] for char in encoded)
    return decoded
 
# Read input
import sys
input = sys.stdin.read
data = input().split()
 
t = int(data[0])
index = 1
results = []
 
for _ in range(t):
    n = int(data[index])
    index += 1
    encoded = data[index]
    index += 1
    results.append(decode_string(encoded))
 
# Output the results
print("\n".join(results))