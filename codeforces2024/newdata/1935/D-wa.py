def main():
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
        beans = list(map(int, data[index:index + n]))
        index += n
        
        # Sort beans by power level in descending order
        beans.sort(reverse=True)
        
        # Select the top k beans and calculate the sum
        max_power = sum(beans[:k])
        
        # Store the result for this test case
        results.append(max_power)
    
    # Output all results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()