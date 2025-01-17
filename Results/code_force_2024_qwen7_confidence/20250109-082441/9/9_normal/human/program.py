def minimum_hamming_distance(t, test_cases):
    results = []
    
    for n, s, t in test_cases:
        # Create good strings
        g1 = ''.join('0' if i % 2 == 0 else '1' for i in range(n))
        g2 = ''.join('1' if i % 2 == 0 else '0' for i in range(n))
        
        # Calculate Hamming distances
        dist1 = sum(1 for i in range(n) if t[i] != g1[i])
        dist2 = sum(1 for i in range(n) if t[i] != g2[i])
        
        # Minimum distance
        results.append(min(dist1, dist2))
    
    return results

# Input example
t = 3
test_cases = [
    (3, "000", "000"),
    (4, "0000", "1111"),
    (6, "111111", "000100")
]

# Output results
print(minimum_hamming_distance(t, test_cases))