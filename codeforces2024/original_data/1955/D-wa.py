def count_good_subsegments(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m, k, a, b = case
        
        # 1. Count frequency of elements in b
        from collections import Counter
        b_counter = Counter(b)
        
        # 2. Initialize the sliding window for a
        current_counter = Counter()
        good_count = 0
        matches = 0
        
        # Start sliding window
        for i in range(n):
            # Add the current element to the current_counter
            current_counter[a[i]] += 1
            
            # If we're at least at the size of m, we need to check
            if i >= m:
                # Remove the element going out of the window
                outgoing_elem = a[i - m]
                current_counter[outgoing_elem] -= 1
                if current_counter[outgoing_elem] == 0:
                    del current_counter[outgoing_elem]
            
            # Only start checking when the window size is m
            if i >= m - 1:
                # Calculate the number of matching elements
                matches = 0
                for num, count in b_counter.items():
                    if num in current_counter:
                        matches += min(current_counter[num], count)
                
                if matches >= k:
                    good_count += 1
        
        results.append(good_count)
    
    return results

# Example usage:
t = 1
test_cases = [
    (5, 3, 2, [1, 2, 1, 3, 2], [2, 2, 1])  # Example case
]
print(count_good_subsegments(t, test_cases))  # Output the results