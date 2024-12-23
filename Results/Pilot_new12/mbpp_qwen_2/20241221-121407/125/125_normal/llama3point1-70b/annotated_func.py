#State of the program right berfore the function call: lst is a list, and n is a positive integer such that n > 0.
def func_1(lst, n):
    return [lst[i::n] for i in range(n)]
    #The program returns a list of sublists, where each sublist is obtained by slicing `lst` starting from index `i` and taking every `n`-th element, for `i` in the range from 0 to `n-1`
#Overall this is what the function does:The function `func_1` accepts a list `lst` and a positive integer `n`, and returns a list of sublists. Each sublist is formed by slicing `lst` starting from index `i` (where `i` ranges from 0 to `n-1`) and taking every `n`-th element thereafter. This means that for each starting index `i`, the sublist contains elements from `lst` at positions `i, i+n, i+2n, ...` until the end of the list. The function handles the case where `n` is greater than the length of `lst`, in which case the corresponding sublist will be empty.

