def find_sequence(n, k):
    # Check if it is possible to express n as a sum of k powers of 2
    if k > n:
        return "No"
    
    # Start by representing n in binary and counting the number of 1s
    bits = []
    for i in range(60, -1, -1):
        if (n >> i) & 1:
            bits.append(i)

    # If the number of bits is more than k, it's impossible
    if len(bits) > k:
        return "No"
    
    # We need to distribute the bits to get exactly k parts
    while len(bits) < k:
        smallest = bits.pop()
        bits.append(smallest - 1)
        bits.append(smallest - 1)
    
    # Sort to ensure that the sequence is lexicographically largest
    bits.sort(reverse=True)
    
    return "Yes\n" + " ".join(map(str, bits))

# Reading input
import sys
input = sys.stdin.read
data = input().strip().split()
n = int(data[0])
k = int(data[1])

# Finding and printing the sequence
print(find_sequence(n, k))
