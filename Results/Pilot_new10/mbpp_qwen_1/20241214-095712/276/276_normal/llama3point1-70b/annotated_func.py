#State of the program right berfore the function call: list1 and list2 are both sorted lists of integers with the same size (size), and size is a positive integer.
def func_1(list1, list2, size):
    merged_list = sorted(list1 + list2)
    middle_index = size - 1
    if (size % 2 == 0) :
        median = (merged_list[middle_index] + merged_list[middle_index + 1]) / 2
    else :
        median = merged_list[middle_index]
    #State of the program after the if-else block has been executed: *`merged_list` is a sorted list of integers formed by merging and sorting `list1` and `list2`; `list1` and `list2` are both sorted lists of integers with the same size (`size`), and `size` is a positive integer; `middle_index` is `size - 1`. If `size` is even, `median` is the average of `merged_list[size - 1]` and `merged_list[size]`. If `size` is odd, `median` is the element at index `size - 1` in `merged_list`.
    return median
    #`The program returns the median of the merged_list, which is the average of merged_list[size - 1] and merged_list[size] if size is even, or the element at index size - 1 if size is odd`
#Overall this is what the function does:The function `func_1` accepts two sorted lists `list1` and `list2` of the same size and a positive integer `size`, and returns the median of the merged and sorted list. Specifically, if `size` is even, it returns the average of the elements at indices `size - 1` and `size` in the merged list. If `size` is odd, it returns the element at index `size - 1` in the merged list.

