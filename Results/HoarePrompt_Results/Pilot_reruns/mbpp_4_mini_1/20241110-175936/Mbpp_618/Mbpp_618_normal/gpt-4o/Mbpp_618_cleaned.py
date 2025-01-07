def func_1(list1, list2):
    return [a / b for (a, b) in zip(list1, list2)]
assert func_1([4, 5, 6], [1, 2, 3]) == [4.0, 2.5, 2.0]
assert func_1([3, 2], [1, 4]) == [3.0, 0.5]
assert func_1([90, 120], [50, 70]) == [1.8, 1.7142857142857142]