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
        k = int(data[index + 1])
        index += 2
        p = list(map(int, data[index:index + n]))
        index += n
        
        # Calculate the initial inversions in q * p when q is the identity permutation
        # q = [1, 2, ..., n]
        # q * p = [p[0], p[1], ..., p[n-1]]
        inv_qp = 0
        for i in range(n):
            for j in range(i + 1, n):
                if p[i] > p[j]:
                    inv_qp += 1
        
        # We need inv(q) + inv(q * p) = k
        # Start with inv(q) = 0, inv(q * p) = inv_qp
        # We need to make inv(q) = k - inv_qp
        target_inv_q = k - inv_qp
        
        if target_inv_q < 0 or target_inv_q > n * (n - 1) // 2:
            results.append("NO")
            continue
        
        # Construct q with exactly target_inv_q inversions
        q = list(range(1, n + 1))
        
        # We can create inversions by reversing parts of the array
        current_inv_q = 0
        for length in range(n, 0, -1):
            if current_inv_q + (length - 1) <= target_inv_q:
                # Reverse the first `length` elements
                q[:length] = reversed(q[:length])
                current_inv_q += (length - 1)
        
        results.append("YES")
        results.append(" ".join(map(str, q)))
    
    sys.stdout.write("\n".join(results) + "\n")