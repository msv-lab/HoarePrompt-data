#State of the program right berfore the function call: lst is a list of elements, and L is a non-negative integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #The program returns a tuple containing the first L elements of the list 'lst' and the remaining elements from index L to the end of the list
#Overall this is what the function does:The function accepts a list `lst` and a non-negative integer `L`, where `0 <= L <= len(lst)`. It returns a tuple consisting of two elements: the first element is a sublist containing the first `L` elements of `lst`, and the second element is a sublist containing the elements from index `L` to the end of `lst`. It effectively divides the input list into two parts based on the given index `L`. If `L` is 0, the first part will be an empty list and the second part will be the entire list. If `L` equals the length of `lst`, the first part will contain all elements and the second part will be empty.

