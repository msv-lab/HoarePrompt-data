#State of the program right berfore the function call: lst is a list of any type, and L is a non-negative integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #The program returns a tuple containing the first L elements of the list 'lst' and the remaining elements from index L to the end of the list
#Overall this is what the function does:The function accepts a list `lst` and a non-negative integer `L`, which must be within the range of the list's length. It returns a tuple consisting of two elements: the first element is a sublist containing the first `L` elements of `lst`, and the second element is a sublist containing the elements from index `L` to the end of `lst`. In edge cases, if `L` is 0, the first element of the returned tuple will be an empty list, and the second element will contain all elements of `lst`. If `L` equals the length of `lst`, the first element will contain all elements of `lst` and the second element will be an empty list. The function does not handle any exceptions related to invalid input types for `lst` or `L`.

