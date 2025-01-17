def get_pairs_count(arr, target_sum):
    count = 0
    freq = {}
    
    for num in arr:
        complement = target_sum - num
        if complement in freq:
            count += freq[complement]
        
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    return count

# Tests
assert get_pairs_count([1,1,1,1],2) == 6
assert get_pairs_count([1,5,7,-1,5],6) == 3
assert get_pairs_count([1,-2,3],1) == 1
assert get_pairs_count([-1,-2,3],-3) == 1
