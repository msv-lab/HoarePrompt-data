#State of the program right berfore the function call: lst is a list of any type, L is a non-negative integer such that 0 <= L <= len(lst).
def func_1(lst, L):
    return lst[:L], lst[L:]
    #The program returns a tuple containing the first L elements of the list 'lst' (lst[:L]) and the remaining elements from index L to the end of the list (lst[L:])
#Overall this is what the function does:The function `func_1` accepts a list `lst` of any type and a non-negative integer `L`, where \(0 \leq L \leq \text{len(lst)}\). It returns a tuple containing two elements: the first element is a list containing the first `L` elements from `lst`, and the second element is a list containing the remaining elements from `lst`, starting from index `L` to the end. Importantly, if `L` is 0, the first element of the tuple will be an empty list and all elements of `lst` will be in the second element. If `L` equals the length of `lst`, the first element of the tuple will contain all elements of `lst` and the second element will be empty. There are no additional checks or error handling for invalid inputs, relying on the precondition provided for `L`.

