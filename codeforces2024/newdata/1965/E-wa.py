def solve():
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
        subarray_sums = list(map(int, data[index:index + (n * (n + 1) // 2 - 1)]))
        index += (n * (n + 1) // 2 - 1)
        
        # We need to find the missing subarray sum
        # Let's assume the missing subarray is the whole array sum
        # We can calculate the expected total sum of all subarray sums if none were missing
        total_subarray_sum = sum(subarray_sums)
        expected_full_subarray_sum = (n * (n + 1) // 2) * (n + 1) // 2
        
        # Calculate the missing sum
        missing_sum = expected_full_subarray_sum - total_subarray_sum
        
        # Now we need to construct a valid palindrome array `a` of size `n`
        # that has all subarray sums as given plus one missing sum that we calculated
        # This is a constructive problem, we need to ensure the array is a palindrome
        # and all subarray sums are possible
        
        # Simplest valid construction for small cases or specific patterns
        # For larger n, we need a more sophisticated method to ensure all sums are possible
        # Here we use a simple heuristic to construct a valid palindrome array
        
        # We start by assuming the array is all ones, which is a simple valid palindrome
        a = [1] * n
        
        # We adjust the array to fit the missing sum by increasing the middle elements
        # since it's a palindrome, we adjust symmetrically
        mid = n // 2
        if n % 2 == 1:  # odd length
            a[mid] += missing_sum
        else:  # even length, distribute the missing sum to the two middle elements
            half_missing = missing_sum // 2
            a[mid - 1] += half_missing
            a[mid] += half_missing
        
        # Output the result for this test case
        results.append(f"{n}")
        results.append(" ".join(map(str, a)))
    
    # Print all results for each test case
    print("\n".join(results))