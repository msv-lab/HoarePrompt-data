#State of the program right berfore the function call: lst is a list of any elements, and L is a non-negative integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #The program returns two slices of the list 'lst': the first slice is from the start of the list to index L (exclusive), and the second slice is from index L to the end of the list.
#Overall this is what the function does:The function accepts a list `lst` and a non-negative integer `L` where `0 <= L <= len(lst)`. It returns two slices of the list: the first slice is the elements from the start of `lst` up to index `L` (exclusive), and the second slice comprises the elements from index `L` to the end of the list. The function correctly handles cases where `L` is 0 (resulting in the first slice being empty) and where `L` equals the length of `lst` (resulting in the second slice being empty). The function does not perform any input validation beyond ensuring that `L` is within the specified bounds.

