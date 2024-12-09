#State of the program right berfore the function call: lst is a list of any elements, and L is a non-negative integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #The program returns two lists: the first being the slice of 'lst' from the start up to index L (exclusive), and the second being the slice of 'lst' from index L to the end.
#Overall this is what the function does:The function accepts a list `lst` and a non-negative integer `L`, and returns two slices: the first being the portion of `lst` from the start up to index `L` (exclusive), and the second being the remainder of `lst` from index `L` to the end. Edge cases include when `L` is 0, in which case the first slice will be empty and the second will be the entire list, and when `L` equals the length of `lst`, resulting in the first slice being the entire list and the second slice being empty.

