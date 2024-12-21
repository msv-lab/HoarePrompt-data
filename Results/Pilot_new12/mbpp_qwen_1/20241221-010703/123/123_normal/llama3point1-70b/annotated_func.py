#State of the program right berfore the function call: lst is a list, and L is an integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #`lst[:L]` which is a sublist of `lst` containing the first L elements, and `lst[L:]` which is a sublist of `lst` containing the remaining elements starting from the Lth element
#Overall this is what the function does:The function `func_1` accepts a list `lst` and an integer `L`. It returns two sublists: the first sublist contains the first `L` elements of `lst`, and the second sublist contains the remaining elements of `lst` starting from the `L`th element. This is achieved using list slicing. If `L` is 0, the first sublist will be an empty list, and the second sublist will contain all elements of `lst`. If `L` is equal to the length of `lst`, the first sublist will contain all elements, and the second sublist will be an empty list. The original list `lst` remains unchanged.

