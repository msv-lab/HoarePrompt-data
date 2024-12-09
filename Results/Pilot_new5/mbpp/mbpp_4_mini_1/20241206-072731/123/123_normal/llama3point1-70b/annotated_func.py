#State of the program right berfore the function call: lst is a list of elements, and L is a non-negative integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #The program returns a tuple consisting of the first L elements of the list 'lst' and the elements from index L to the end of the list 'lst', where L is a non-negative integer such that 0 <= L <= len(lst).
#Overall this is what the function does:The function accepts a list `lst` and a non-negative integer `L`, and returns a tuple containing the first `L` elements of `lst` and the elements from index `L` to the end of `lst`. It correctly handles cases where `L` is 0 or equal to the length of the list, returning an empty list for the first part or the entire list for the second part, respectively.

