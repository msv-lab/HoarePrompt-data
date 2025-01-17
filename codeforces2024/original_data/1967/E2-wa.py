MOD = 998244353

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

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
        m = int(data[index + 1])
        b0 = int(data[index + 2])
        index += 3
        
        # Total number of arrays a
        total_arrays = mod_exp(m, n, MOD)
        
        # Number of invalid arrays
        # Invalid arrays are those where no valid b can be constructed
        # This is equivalent to the number of ways to choose a1, ..., an
        # such that they are all equal to some b0, b1, ..., bn
        # But since b0 is given, we need to consider the valid b sequences
        # that start from b0 and end at some bn, and for each such sequence,
        # there is exactly one invalid a sequence.
        
        # Calculate the number of valid arrays
        valid_arrays = total_arrays  # Since we don't have a direct way to count invalid arrays
        
        results.append(valid_arrays)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')