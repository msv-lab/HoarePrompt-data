#State of the program right berfore the function call: lst is a list of any type, and n is a positive integer such that 0 < n <= len(lst).
def func_1(lst, n):
    return [lst[i::n] for i in range(n)]
    #[[lst[0], lst[3], lst[6], ...], [lst[1], lst[4], lst[7], ...], [lst[2], lst[5], lst[8], ...]]
#Overall this is what the function does:The function `func_1` accepts a list `lst` and a positive integer `n`, and returns a list of lists where each sublist contains elements from `lst` at indices that are multiples of `n`. Specifically, the function generates `n` sublists, each containing elements from `lst` at positions that are multiples of their respective index (i.e., starting from index `i` and taking every `n`th element thereafter). This operation is performed for each starting index from `0` to `n-1`. If `lst` is empty or `n` is `0`, the function will raise an error since `0 < n <= len(lst)` is a precondition. The function handles the case where `n` is equal to `1` by returning a list containing the original `lst` as the only sublist. If `n` is equal to the length of `lst`, the function returns a list of sublists where each sublist contains exactly one element from `lst`.

