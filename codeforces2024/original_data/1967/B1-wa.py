import sys
import math

input = sys.stdin.read
data = input().split()

def solve():
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        count = 0
        
        # Iterate over each possible b
        for b in range(1, m + 1):
            # Iterate over each possible gcd value
            for g in range(1, n // b + 1):
                # a must be a multiple of g
                # a = k * g where k is an integer
                # a + b = k * g + b must be a multiple of b * g
                # k * g + b = j * b * g for some integer j
                # k * g = j * b * g - b
                # k = j * b - 1
                # k * g <= n
                # (j * b - 1) * g <= n
                # j * b * g <= n + g
                # j <= (n + g) // (b * g)
                
                max_j = (n + g) // (b * g)
                count += max_j
        
        results.append(count)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

solve()