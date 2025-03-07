def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index+n]))
        index += n
        
        # Start with the first sign
        last_year = a[0]
        
        # Process each subsequent sign
        for i in range(1, n):
            # Calculate the next possible year for the current sign
            # It must be greater than last_year
            next_year = ((last_year + 1 + a[i] - 1) // a[i]) * a[i]
            last_year = next_year
        
        # The year the last sign occurs is the answer for this test case
        results.append(str(last_year))
    
    # Output all results
    sys.stdout.write("\n".join(results) + "\n")
 
if __name__ == "__main__":
    main()