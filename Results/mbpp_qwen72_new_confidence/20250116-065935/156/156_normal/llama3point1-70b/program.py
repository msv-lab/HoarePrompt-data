def large_product(list1, list2, n):
    products = [a * b for a in list1 for b in list2]
    return sorted(products, reverse=True)[:n]
