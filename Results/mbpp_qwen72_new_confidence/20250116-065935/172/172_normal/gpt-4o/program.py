def min_product_tuple(pairs):
    # Initialize the minimum product with a large value
    min_product = float('inf')
    
    # Iterate through each pair in the list
    for pair in pairs:
        # Calculate the product of the current pair
        product = pair[0] * pair[1]
        # Update the minimum product if the current product is smaller
        if product < min_product:
            min_product = product
    
    return min_product

# Testing the function with the provided test cases
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] ) == 8
assert min_product_tuple([(10,20), (15,2), (5,10)] ) == 30
assert min_product_tuple([(11,44), (10,15), (20,5), (12, 9)] ) == 100
