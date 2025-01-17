def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        m = int(data[index])
        k = int(data[index + 1])
        index += 2
        
        f = list(map(int, data[index:index + m + 1]))
        index += m + 1
        
        mex = 0
        while mex <= m and f[mex] > 0:
            # Alice picks one of `mex`
            f[mex] -= 1
            
            # Bob removes up to `k` elements
            remaining_k = k
            for i in range(mex + 1):
                if remaining_k <= 0:
                    break
                if f[i] > 0:
                    remove = min(f[i], remaining_k)
                    f[i] -= remove
                    remaining_k -= remove
            
            mex += 1
        
        results.append(mex)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')