#State of the program right berfore the function call: list1 and list2 are lists of integers, both of the same size, and size is a positive integer representing the length of the lists.
def func_1(list1, list2, size):
    merged_list = sorted(list1 + list2)
    middle_index = size - 1
    if (size % 2 == 0) :
        median = (merged_list[middle_index] + merged_list[middle_index + 1]) / 2
    else :
        median = merged_list[middle_index]
    #State of the program after the if-else block has been executed: *`list1` and `list2` are lists of integers, and `size` is a positive integer. If `size` is even, `median` is calculated as the average of the two middle values in the sorted `merged_list`. If `size` is odd, `median` is the middle value at index `middle_index` in the sorted `merged_list`.
    return median
    #The program returns the median value of the combined lists `list1` and `list2`, calculated based on whether `size` is even or odd. If `size` is even, the median is the average of the two middle values; if odd, it is the middle value at index `middle_index` in the sorted `merged_list`.
#Overall this is what the function does:The function accepts two lists of integers (`list1` and `list2`) and an integer (`size`), representing the length of the lists. It merges the two lists, sorts them, and calculates the median value. If `size` is even, the median is calculated as the average of the two middle values; if odd, it is the middle value in the sorted merged list. The function does not handle cases where `size` does not accurately reflect the length of `list1` and `list2`, nor does it check if the lists are empty, which could lead to an index error.

