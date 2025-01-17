def find_remainder(arr, n):
    product = 1
    for num in arr:
        product *= num
    return product % n

# Running the provided tests
assert find_remainder([100, 10, 5, 25, 35, 14], 11) == 9
assert find_remainder([1, 1, 1], 1) == 0
assert find_remainder([1, 2, 1], 2) == 0
