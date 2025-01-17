def unique_product(numbers):
    unique_nums = set(numbers)
    product = 1
    for num in unique_nums:
        product *= num
    return product
