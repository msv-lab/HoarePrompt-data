import sys
input = sys.stdin.read
from collections import defaultdict
from bisect import bisect_left
 
def solve():
    data = input().split()
    index = 0
    
    # Read number of test cases
    t = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        # Read n and q
        n = int(data[index])
        q = int(data[index + 1])
        index += 2
        
        # Read the array
        a = [0] * (n + 1)
        pf = [0] * (n + 1)
        mp = defaultdict(list)
        
        mp[0].append(0)
        
        for i in range(1, n + 1):
            a[i] = int(data[index])
            index += 1
            pf[i] = pf[i - 1] ^ a[i]
            mp[pf[i]].append(i)
        
        for _ in range(q):
            l = int(data[index])
            r = int(data[index + 1])
            index += 2
            
            x = pf[r] ^ pf[l - 1]
            if x == 0:
                results.append("YES")
                continue
            
            # Access lists v1 and v2 from map mp
            v1 = mp[pf[r]]
            v2 = mp[pf[l - 1]]
            
            # Find the range within v1 and v2
            it1 = bisect_left(v1, l)
            it2 = bisect_left(v2, r) - 1
            
            # Check if the found indices are valid and satisfy the condition
            if it1 < len(v1) and it2 >= 0 and v1[it1] < v2[it2]:
                results.append("YES")
            else:
                results.append("NO")
    
    # Print all results at the end
    print("\n".join(results))
 
# Run the solve function
solve()