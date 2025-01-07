#State of the program right berfore the function call: list1 and list2 are both sorted lists of integers with the same size n, and n is a positive integer.
def func_1(list1, list2, n):
    merged_list = sorted(list1 + list2)
    mid = len(merged_list) // 2
    if (len(merged_list) % 2 == 0) :
        median = (merged_list[mid - 1] + merged_list[mid]) / 2
    else :
        median = merged_list[mid]
    #State of the program after the if-else block has been executed: *`list1` is a sorted list of integers with size n, `list2` is a sorted list of integers with size n, `merged_list` is a sorted list of integers with size 2n, `mid` is n. If the length of `merged_list` is even, `median` is (merged_list[n - 1] + merged_list[n]) / 2. If the length of `merged_list` is odd, `median` is equal to `merged_list[n]`.
    return median
    #The program returns median which is calculated as (merged_list[mid - 1] + merged_list[mid]) / 2 if the length of merged_list is even, or merged_list[mid] if the length of merged_list is odd, where mid is n
#Overall this is what the function does:The function `func_1` accepts two sorted lists `list1` and `list2` of the same size `n`, merges them into a single sorted list `merged_list`, and returns the median of this merged list. If the length of `merged_list` is even, the median is the average of the two middle elements; if the length is odd, the median is the middle element.

