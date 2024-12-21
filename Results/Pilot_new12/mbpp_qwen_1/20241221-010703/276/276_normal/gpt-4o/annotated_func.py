#State of the program right berfore the function call: list1 and list2 are both sorted lists of integers with the same length n.
def func_1(list1, list2, n):
    merged_list = sorted(list1 + list2)
    mid = len(merged_list) // 2
    if (len(merged_list) % 2 == 0) :
        median = (merged_list[mid - 1] + merged_list[mid]) / 2
    else :
        median = merged_list[mid]
    #State of the program after the if-else block has been executed: *`list1` and `list2` are both sorted lists of integers with the same length `n`; `merged_list` is a sorted list of length `2n` containing elements from `list1` and `list2` in ascending order; `mid` is `n`. If the length of `merged_list` is even, the median is the average of `merged_list[mid - 1]` and `merged_list[mid]`. Otherwise, the median is the element at index `n` in `merged_list`.
    return median
    #The program returns the median of the merged list, which is the average of `merged_list[mid - 1]` and `merged_list[mid]` if the length of `merged_list` is even, or the element at index `n` in `merged_list` if the length is odd.
#Overall this is what the function does:The function `func_1` accepts two sorted lists of integers, `list1` and `list2`, both of length `n`. It merges these two lists into a single sorted list called `merged_list`. The function then calculates and returns the median of `merged_list`. If the length of `merged_list` is even, the median is the average of the two middle elements (`merged_list[mid - 1]` and `merged_list[mid]`). If the length is odd, the median is the middle element (`merged_list[mid]`). This calculation is done after merging the lists, regardless of whether the individual lists were originally even or odd in length.

