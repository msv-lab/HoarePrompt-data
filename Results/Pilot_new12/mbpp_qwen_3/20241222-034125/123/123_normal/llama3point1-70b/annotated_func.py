#State of the program right berfore the function call: lst is a list, and L is an integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #`lst[:L]` is a slice of `lst` up to index `L`, and `lst[L:]` is a slice of `lst` starting from index `L` to the end
#Overall this is what the function does:The function `func_1` accepts a list `lst` and an integer `L`, where `0 <= L <= len(lst)`. It returns a tuple containing two slices: the first slice is a part of `lst` from the start up to but not including index `L`, and the second slice is the remaining part of `lst` starting from index `L` to the end. This function ensures that the original list `lst` remains unchanged and only the slices are returned. If `L` is `0`, the first slice will be an empty list, and if `L` is equal to `len(lst)`, the second slice will be an empty list.

