#State of the program right berfore the function call: lst is a list of any types, and n is a positive integer such that n > 0.
def func_1(lst, n):
    return [lst[i::n] for i in range(n)]
    #[[lst[0], lst[3], lst[6], ...], [lst[1], lst[4], lst[7], ...], [lst[2], lst[5], lst[8], ...]]
#Overall this is what the function does:The function `func_1` accepts a list `lst` of any types and a positive integer `n`. It returns a list of `n` sublists, where each sublist contains every `n`-th element from the original list `lst`, starting from indices 0, 1, 2, ..., up to `n-1` respectively. Specifically, the first sublist starts at index 0, the second at index 1, and so on. This operation ensures that each element in the original list `lst` appears exactly once in one of the sublists. If the length of `lst` is not a multiple of `n`, the last sublist will contain fewer elements than the others.

