#State of the program right berfore the function call: lst is a list, L is a non-negative integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #The program returns a tuple of two lists: the first list contains the first L elements of `lst`, and the second list contains the remaining elements of `lst`.
#Overall this is what the function does:The function accepts a list `lst` and a non-negative integer `L`, and returns a tuple of two lists where the first list contains the first `L` elements of `lst` and the second list contains the remaining elements of `lst`; if `L` is greater than or equal to the length of `lst`, the first list contains all elements of `lst` and the second list is empty; if `L` is 0, the first list is empty and the second list contains all elements of `lst`; if `lst` is empty, both lists in the tuple are empty.

