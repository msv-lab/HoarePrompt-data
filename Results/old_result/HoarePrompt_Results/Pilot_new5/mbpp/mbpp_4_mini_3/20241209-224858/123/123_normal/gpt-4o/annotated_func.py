#State of the program right berfore the function call: lst is a list of elements, and L is a non-negative integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #The program returns a tuple consisting of two lists: the first list is a slice of 'lst' from the beginning up to index L, and the second list is a slice of 'lst' from index L to the end.
#Overall this is what the function does:The function accepts a list `lst` and a non-negative integer `L`. It returns a tuple containing two lists: the first list is a slice of `lst` from the beginning up to index `L` (inclusive of index `L-1`), and the second list is a slice of `lst` from index `L` to the end. If `L` is equal to the length of `lst`, the first list will contain all elements, and the second list will be empty. If `L` is 0, the first list will be empty, and the second list will contain all elements of `lst`.

