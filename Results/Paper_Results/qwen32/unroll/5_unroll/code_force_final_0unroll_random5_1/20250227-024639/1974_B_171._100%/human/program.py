def decode_string(encoded):
    # Step 1: Extract unique characters from the encoded string and sort them to form r
    unique_chars = sorted(set(encoded))
    
    # Step 2: Create a mapping from each character in r to its symmetric counterpart
    char_map = {}
    len_unique = len(unique_chars)
    for i in range(len_unique):
        char_map[unique_chars[i]] = unique_chars[len_unique - 1 - i]
    
    # Step 3: Decode the encoded string b using the mapping
    decoded = ''.join(char_map[ch] for ch in encoded)
    
    return decoded
 
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
 
# Printing output
for result in results:
    print(result)