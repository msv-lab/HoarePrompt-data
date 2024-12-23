#State of the program right berfore the function call: lst is a list, and L is an integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #`The program returns two lists: the first list contains elements from the start of lst up to but not including the element at index L, and the second list contains elements from index L to the end of lst`
#Overall this is what the function does:The function `func_1` accepts a list `lst` and an integer `L` as parameters. It returns two lists: the first list contains all elements from the start of `lst` up to but not including the element at index `L`, and the second list contains all elements from index `L` to the end of `lst`. This division is performed using list slicing, which handles edge cases such as when `L` is 0 (returning an empty list for the first slice and the entire list for the second) or when `L` equals the length of `lst` (returning the entire list for the first slice and an empty list for the second).

