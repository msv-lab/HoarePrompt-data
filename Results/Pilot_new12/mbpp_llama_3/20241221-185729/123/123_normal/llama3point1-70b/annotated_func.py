#State of the program right berfore the function call: lst is a list and L is a non-negative integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #The program returns a tuple containing two lists: the first list contains the first L elements of 'lst' and the second list contains the remaining elements of 'lst'.
#Overall this is what the function does:The function accepts a list `lst` and a non-negative integer `L`, and returns a tuple of two lists. The first list in the tuple contains the first `L` elements of `lst`, and the second list contains the remaining elements of `lst`. If `L` is 0, the first list will be empty and the second list will be the entire original list. If `L` equals the length of `lst`, the first list will contain all elements of `lst` and the second list will be empty. The function effectively splits the input list `lst` into two parts at the index `L`, without modifying the original list.

