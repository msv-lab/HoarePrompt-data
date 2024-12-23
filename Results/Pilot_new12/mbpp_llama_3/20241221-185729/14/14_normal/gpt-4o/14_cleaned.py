def func_1(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False
assert func_1([1, 2, 3, 4, 5]) == False
assert func_1([1, 2, 3, 4, 4]) == True
assert func_1([1, 1, 2, 2, 3, 3, 4, 4, 5]) == True