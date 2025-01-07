#State of the program right berfore the function call: list1 and list2 are two sorted lists of integers of the same size, and n is a positive integer equal to the length of either list1 or list2.
def func_1(list1, list2, n):
    merged_list = sorted(list1 + list2)
    mid = len(merged_list) // 2
    if (len(merged_list) % 2 == 0) :
        median = (merged_list[mid - 1] + merged_list[mid]) / 2
    else :
        median = merged_list[mid]
    #State of the program after the if-else block has been executed: *`list1` and `list2` are two sorted lists of integers of the same size; `n` is a positive integer; `merged_list` is a sorted list combining `list1` and `list2`; `mid` is equal to `n`. If the length of `merged_list` is even, then `median` is equal to (merged_list[n - 1] + merged_list[n]) / 2. Otherwise, `median` is equal to `merged_list[n]`.
    return median
    #The program returns the median of the merged list, which is calculated based on whether the length of `merged_list` is even or odd. If it is even, the program returns the average of the two middle elements; if it is odd, the program returns the middle element.
#Overall this is what the function does:The function accepts two sorted lists of integers (`list1` and `list2`) and a positive integer `n`, which represents the length of either list. It merges `list1` and `list2` into a new sorted list and calculates the median of this merged list. If the merged list has an even length, the function correctly returns the average of the two middle elements; if the merged list has an odd length, it returns the middle element. The function assumes that both input lists are of the same size and does not handle cases where the lists might be empty or of different lengths.

