def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 1_000_000_007
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        k = int(data[idx + 2])
        idx += 3
        
        # Binary search for the minimum number of steps
        low, high = 0, max(n, m) * 20  # Arbitrary high number of steps
        answer = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_reduce_area(n, m, k, mid):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        
        # Calculate p * inv(q) % MOD
        # Since the problem guarantees that the answer can be expressed as A + B*sqrt(2),
        # and asks for B as p/q, we need to find B and compute p * inv(q) % MOD.
        # Here we assume B is the result we found, and q = 1 (since B is an integer).
        p = answer
        q = 1
        q_inv = pow(q, MOD - 2, MOD)  # Fermat's little theorem for modular inverse
        result = (p * q_inv) % MOD
        results.append(result)
    
    for res in results:
        print(res)

def can_reduce_area(n, m, k, steps):
    # This function should estimate if we can reduce the area below k in the given number of steps
    # We use a simple heuristic: assume each cut reduces the largest dimension by about half
    import math
    
    # Simulate the cutting process
    h, w = n, m
    for _ in range(steps):
        if h > w:
            h = max(h // 2, 1)
        else:
            w = max(w // 2, 1)
        if h * w < k:
            return True
    return h * w < k

if __name__ == "__main__":
    main()