#State of the program right berfore the function call: list1 and list2 are lists of integers of the same size, and n is a positive integer representing the size of the lists (n > 0).
def func_1(list1, list2, n):
    merged_list = sorted(list1 + list2)
    mid = len(merged_list) // 2
    if (len(merged_list) % 2 == 0) :
        median = (merged_list[mid - 1] + merged_list[mid]) / 2
    else :
        median = merged_list[mid]
    #State of the program after the if-else block has been executed: *`list1` and `list2` are lists of integers of the same size, `n` is a positive integer representing the size of the lists (n > 0), and `merged_list` is the sorted combination of `list1` and `list2`. If the length of `merged_list` is even, the median is calculated as (merged_list[mid - 1] + merged_list[mid]) / 2. Otherwise, the median is equal to `merged_list[n]`.
    return median
    #The program returns the median of the sorted combination of 'list1' and 'list2', which is calculated based on the size of 'merged_list', being either the average of the two middle values if 'merged_list' is even, or the middle value if 'merged_list' is odd.
#Overall this is what the function does:The function accepts two lists of integers (`list1` and `list2`) of the same size, and a positive integer `n` representing the size of the lists. It returns the median of the sorted combination of these two lists. If the merged list is of even length, it calculates the median as the average of the two middle values; if it is of odd length, it returns the middle value. The function does not perform any checks for the input validity, meaning it assumes that both lists are non-empty and of the same length as specified by `n`.

