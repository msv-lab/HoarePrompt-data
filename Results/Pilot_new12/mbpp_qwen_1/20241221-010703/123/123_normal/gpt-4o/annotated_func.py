#State of the program right berfore the function call: lst is a list, and L is an integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #`lst[:L]` is the slice of `lst` from the start up to but not including index `L`, and `lst[L:]` is the slice of `lst` starting from index `L` to the end
#Overall this is what the function does:The function `func_1` accepts a list `lst` and an integer `L`. It returns two slices of the list: the first slice contains elements from the start of the list up to but not including index `L`, and the second slice contains elements from index `L` to the end of the list. If `L` is 0, the first slice is empty and the second slice is the entire list. If `L` is equal to the length of the list, the first slice is the entire list and the second slice is empty. If `L` is greater than the length of the list, only the first slice is returned, which is the entire list, and the second slice is not returned.

