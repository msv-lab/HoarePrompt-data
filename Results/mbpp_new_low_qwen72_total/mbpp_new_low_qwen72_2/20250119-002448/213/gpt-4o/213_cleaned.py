def func_1(arr):
    n = len(arr)
    if n == 0:
        return 0
    max_products = [0] * n
    max_products[0] = arr[0]
    for i in range(1, n):
        max_products[i] = arr[i]
        for j in range(i):
            if arr[j] < arr[i]:
                max_products[i] = max(max_products[i], max_products[j] * arr[i])
    return max(max_products)
assert func_1([3, 100, 4, 5, 150, 6]) == 3000
assert func_1([4, 42, 55, 68, 80]) == 50265600
assert func_1([10, 22, 9, 33, 21, 50, 41, 60]) == 2460