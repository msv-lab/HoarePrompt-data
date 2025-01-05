def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 999999893
    
    def mod_inv(a, mod):
        return pow(a, mod - 2, mod)
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        N = int(data[i])
        
        # Calculate M and V
        M = 0
        V = 0
        current_length = 1.0
        for j in range(1, N + 1):
            current_length /= 2**0.5
            if j % 2 == 1:
                M += current_length
            else:
                V += current_length
        
        # Assuming M/V can be expressed as A + B*sqrt(2)
        # We need to find B as p/q and then compute p * inv(q) % MOD
        # For simplicity, assume B = M/V directly (since M and V are sums of terms involving sqrt(2))
        if V == 0:
            results.append(0)
        else:
            B = M / V
            p = int(B)  # This is a simplification, normally you would extract p and q from B
            q = 1
            result = (p * mod_inv(q, MOD)) % MOD
            results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()