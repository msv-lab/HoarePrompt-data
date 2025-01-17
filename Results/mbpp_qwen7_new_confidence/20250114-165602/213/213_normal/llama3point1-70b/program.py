def max_product(nums):
    n = len(nums)
    max_product = [1] * n
    min_product = [1] * n
    
    for i in range(1, n):
        if nums[i-1] < nums[i]:
            max_product[i] = max_product[i-1] * nums[i]
        else:
            max_product[i] = nums[i]
    
    result = max(max_product)
    
    return result
