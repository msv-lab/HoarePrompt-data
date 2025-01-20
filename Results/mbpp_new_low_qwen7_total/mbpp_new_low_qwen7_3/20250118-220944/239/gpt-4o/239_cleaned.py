def func_1(lst):
    count = Counter(lst)
    result = [num for num in lst if count[num] == 1]
    return result
assert func_1([1, 2, 3, 2, 3, 4, 5]) == [1, 4, 5]
assert func_1([1, 2, 3, 2, 4, 5]) == [1, 3, 4, 5]
assert func_1([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]