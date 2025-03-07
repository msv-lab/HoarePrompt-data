def count_beautiful_pairs(test_cases):
    results = []
    
    for n, x, y, arr in test_cases:
        freq = {}
        count = 0
        
        for a in arr:
            # Calculate required remainders
            rx = (-a % x + x) % x  # Required remainder for x
            ry = a % y             # Required remainder for y
            
            # Count pairs matching the remainders
            if (rx, ry) in freq:
                count += freq[(rx, ry)]
            
            # Update frequency of current remainders
            current_pair = (a % x, a % y)
            if current_pair in freq:
                freq[current_pair] += 1
            else:
                freq[current_pair] = 1
        
        results.append(count)
    
    return results
 
 
# Input and output handling
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
 
    t = int(data[0])
    test_cases = []
    idx = 1
 
    for _ in range(t):
        n, x, y = map(int, data[idx].split())
        arr = list(map(int, data[idx + 1].split()))
        test_cases.append((n, x, y, arr))
        idx += 2
 
    results = count_beautiful_pairs(test_cases)
 
    for result in results:
        print(result)
 
 
if __name__ == "__main__":
    main()