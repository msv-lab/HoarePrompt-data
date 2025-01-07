def func_1(list_of_lists):
    first_elements = [sublist[0] for sublist in list_of_lists]
    second_elements = [sublist[1] for sublist in list_of_lists]
    return [first_elements, second_elements]
assert func_1([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
assert func_1([[1, 2], [3, 4], [5, 6], [7, 8]]) == [[1, 3, 5, 7], [2, 4, 6, 8]]
assert func_1([[[1], [2]], [[3], [4]], [[5], [6]], [[7], [8]]]) == [[[1], [3], [5], [7]], [[2], [4], [6], [8]]]
print('All test cases passed!')