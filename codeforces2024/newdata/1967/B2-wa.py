def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MAX_N = 2000000
    
    # Precompute the number of valid (a', b') pairs for each sum s = a' + b'
    valid_pairs = [0] * (MAX_N + 1)
    
    for a_prime in range(1, MAX_N + 1):
        for b_prime in range(a_prime, MAX_N + 1, a_prime):
            s = a_prime + b_prime
            if s <= MAX_N:
                valid_pairs[s] += 1
    
    # Read input
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        count = 0
        
        # Iterate over possible gcd values
        for g in range(1, min(n, m) + 1):
            max_a_prime = n // g
            max_b_prime = m // g
            
            # Count valid (a', b') pairs where a' + b' <= max_a_prime + max_b_prime
            for s in range(2, max_a_prime + max_b_prime + 1):
                if s <= MAX_N:
                    count += valid_pairs[s]
        
        results.append(count)
    
    # Output results
    sys.stdout.write('\n'.join(map(str, results)) + '\n')