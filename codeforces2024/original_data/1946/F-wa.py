def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 10**9 + 7
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Calculate the initial sum of the array
        total_sum = sum(a) % MOD
        
        # Function to find the maximum subarray sum using Kadane's algorithm
        def kadane(arr):
            max_ending_here = max_so_far = arr[0]
            for x in arr[1:]:
                max_ending_here = max(x, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far
        
        # Find the maximum subarray sum
        max_subarray_sum = kadane(a)
        
        # If the maximum subarray sum is positive, we can use it k times
        if max_subarray_sum > 0:
            max_increase = (max_subarray_sum * k) % MOD
            result = (total_sum + max_increase) % MOD
        else:
            # If no positive gain, the best sum is the initial sum
            result = total_sum
        
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()