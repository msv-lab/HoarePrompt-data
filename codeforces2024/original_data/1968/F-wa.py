def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        q = int(data[index + 1])
        index += 2
        
        a = list(map(int, data[index:index + n]))
        index += n
        
        # Compute prefix XOR
        prefix_xor = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_xor[i] = prefix_xor[i - 1] ^ a[i - 1]
        
        for __ in range(q):
            l = int(data[index])
            r = int(data[index + 1])
            index += 2
            
            # Convert to 0-based index
            l -= 1
            r -= 1
            
            # XOR of the subarray a[l:r+1]
            subarray_xor = prefix_xor[r + 1] ^ prefix_xor[l]
            
            if subarray_xor == 0:
                results.append("YES")
            else:
                # Check if there is a point in the subarray where prefix_xor is the same as subarray_xor
                found = False
                for i in range(l, r):
                    if prefix_xor[i + 1] == subarray_xor:
                        found = True
                        break
                if found:
                    results.append("YES")
                else:
                    results.append("NO")
    
    sys.stdout.write("\n".join(results) + "\n")