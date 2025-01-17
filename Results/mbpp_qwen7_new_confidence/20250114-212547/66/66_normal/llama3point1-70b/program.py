def max_product_tuple(tuple_list):
    max_product = 0
    for tup in tuple_list:
        product = abs(tup[0] * tup[1])
        if product > max_product:
            max_product = product
    return max_product
