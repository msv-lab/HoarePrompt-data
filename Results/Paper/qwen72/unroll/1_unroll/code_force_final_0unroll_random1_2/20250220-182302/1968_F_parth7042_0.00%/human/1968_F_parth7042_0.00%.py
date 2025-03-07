import sys
input = sys.stdin.read
import bisect
 
def solve():
    data = input().split()
    idx = 0
    
    # Read the number of test cases
    t = int(data[idx])
    idx += 1
 
    results = []
    
    # Process each test case
    for _ in range(t):
        # Read n (length of array) and q (number of queries)
        n = int(data[idx])
        q = int(data[idx + 1])
        idx += 2
        
        # Read the array `a`
        a = [0] * (n + 1)
        pf = [0] * (n + 1)
        
        # Dictionary to store occurrences of XOR values
        mp = {0: [0]}
        
        # Calculate prefix XOR array and update dictionary
        for i in range(1, n + 1):
            a[i] = int(data[idx])
            idx += 1
            pf[i] = pf[i - 1] ^ a[i]
            if pf[i] not in mp:
                mp[pf[i]] = []
            mp[pf[i]].append(i)
 
        # Process each query
        for _ in range(q):
            l = int(data[idx])
            r = int(data[idx + 1])
            idx += 2
 
            # Calculate XOR between pf[r] and pf[l - 1]
            x = pf[r] ^ pf[l - 1]
 
            # If XOR is zero, print "YES" immediately
            if x == 0:
                results.append("YES")
                continue
 
            # Get lists of indices for the XOR values
            v1 = mp.get(pf[r], [])
            v2 = mp.get(pf[l - 1], [])
 
            # Use bisect to find positions in the lists
            it1 = bisect.bisect_left(v1, l)
            it2 = bisect.bisect_left(v2, r) - 1
            
            # Compare positions and print the result
            if it1 < len(v1) and it2 >= 0 and v1[it1] <= r and v2[it2] >= l:
                results.append("YES")
            else:
                results.append("NO")
 
        # Add a newline for separation
        results.append("")
    
    # Print all results
    print("\n".join(results))
 
if __name__ == "__main__":
    solve()