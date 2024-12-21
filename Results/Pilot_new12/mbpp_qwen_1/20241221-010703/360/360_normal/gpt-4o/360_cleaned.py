def func_1(list_of_lists):
    max_sum = float('-inf')
    max_list = []
    for sublist in list_of_lists:
        current_sum = sum(sublist)
        if current_sum > max_sum:
            max_sum = current_sum
            max_list = sublist
    return max_list
assert func_1([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]) == [10, 11, 12]
assert func_1([[3, 2, 1], [6, 5, 4], [12, 11, 10]]) == [12, 11, 10]
assert func_1([[2, 3, 1]]) == [2, 3, 1]