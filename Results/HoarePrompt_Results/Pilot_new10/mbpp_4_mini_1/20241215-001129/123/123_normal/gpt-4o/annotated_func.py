#State of the program right berfore the function call: lst is a list of any type, and L is a non-negative integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #The program returns a tuple consisting of the first L elements of the list 'lst' and the remaining elements from index L onward, where L is a non-negative integer such that 0 <= L <= len(lst).
#Overall this is what the function does:The function accepts a list `lst` and a non-negative integer `L` (where `0 <= L <= len(lst)`). It returns a tuple containing the first `L` elements of the list `lst` and the remaining elements from index `L` onward. If `L` is equal to 0, the first part of the tuple will be empty, and if `L` is equal to the length of `lst`, the second part will be empty.

