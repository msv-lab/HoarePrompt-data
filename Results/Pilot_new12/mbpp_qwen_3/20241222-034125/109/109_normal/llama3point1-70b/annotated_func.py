#State of the program right berfore the function call: list1 and list2 are both lists.
def func_1(list1, list2):
    if list1 :
        list1[-1:] = list2
    else :
        list1 = list2
    #State of the program after the if-else block has been executed: `list1` and `list2` are both lists. If `list1` is not empty, its last element is replaced by all elements of `list2`, and `list2` remains unchanged. If `list1` is an empty list, `list1` references the same list object as `list2`, and `list2` retains its original state.
    return list1
    #`list1` references the same list object as `list2` if `list1` is empty, otherwise the last element of `list1` is replaced by all elements of `list2` and `list1` contains those elements, while `list2` remains unchanged
#Overall this is what the function does:The function `func_1` accepts two parameters, `list1` and `list2`, both of which are lists. It modifies `list1` based on whether it is empty or not. If `list1` is empty, it replaces `list1` with `list2`, making them reference the same list object. If `list1` is not empty, it replaces only the last element of `list1` with all elements of `list2`, while ensuring `list2` remains unchanged. This means that after the function execution, `list1` will either reference the same list as `list2` if `list1` was initially empty, or the last element of `list1` will be updated to the contents of `list2`, and `list2` will remain unaltered.

