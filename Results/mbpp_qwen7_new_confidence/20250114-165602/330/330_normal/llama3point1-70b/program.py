def get_pairs_count(nums, total_sum):
    num_count = {}
    pairs_count = 0
    
    for num in nums:
        complement = total_sum - num
        if complement in num_count:
            pairs_count += num_count[complement]
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    return pairs_count
