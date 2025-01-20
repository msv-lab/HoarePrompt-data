#State of the program right berfore the function call: lst is a list of any type, and n is a positive integer such that n > 0.
def func_1(lst, n):
    result = [[] for _ in range(n)]
    for (i, element) in enumerate(lst):
        result[i % n].append(element)
        
    #State of the program after the  for loop has been executed: `i` is equal to the length of `lst`; each `result[j]` (where `j` ranges from 0 to `n-1`) contains elements from `lst` starting from `j` and stepping by `n`.
    return result
    #`result` is a list of sublists from `lst`, where `result[j]` contains elements from `lst` starting from index `j` and stepping by `i`
#Overall this is what the function does:The function `func_1` accepts a list `lst` and a positive integer `n`. It returns a list of `n` sublists, where each sublist contains elements from `lst` starting from an index `j` (with `j` ranging from 0 to `n-1`) and stepping by `n`. Specifically, `result[j]` contains elements from `lst` starting from index `j` and then every `n`th element thereafter until the end of the list is reached. If the length of `lst` is not a multiple of `n`, the last sublist may contain fewer than `n` elements.

