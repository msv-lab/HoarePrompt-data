def is_product_even(nums):
    product = 1
    for num in nums:
        product *= num
    return product % 2 == 0
