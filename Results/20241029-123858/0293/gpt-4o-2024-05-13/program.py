def find_tables(x):
    results = []
    
    # Iterate over possible n values
    for n in range(1, int(x**0.5) + 1):
        m = 0
        total_squares = 0
        
        # Iterate over possible square sizes
        while total_squares < x:
            m += 1
            total_squares += (n - m + 1) * (m - n + 1)
            
            if total_squares == x:
                results.append((n, m))
                break
    
    # Print the results
    print(len(results))
    for n, m in sorted(results):
        print(n, m)

# Read input
x = int(input().strip())

# Find and print the tables
find_tables(x)
