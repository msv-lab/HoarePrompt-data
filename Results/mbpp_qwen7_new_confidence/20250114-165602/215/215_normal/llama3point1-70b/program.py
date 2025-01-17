def find_remainder(nums, n):
    product = 1
    for num in nums:
        product = (product * num) % n
    return product
