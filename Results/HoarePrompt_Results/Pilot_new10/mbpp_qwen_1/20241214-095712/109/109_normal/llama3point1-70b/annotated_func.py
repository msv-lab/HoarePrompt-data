#State of the program right berfore the function call: list1 and list2 are both lists.
def func_1(list1, list2):
    if list1 :
        list1[-1:] = list2
    else :
        list1 = list2
    #State of the program after the if-else block has been executed: *`list1` and `list2` are both lists. If `list1` is not empty, its last element is updated to match `list2`, while `list2` retains its original values. If `list1` is empty, `list1` references the same list object as `list2`, and `list2` retains its original contents.
    return list1
    #`list1` contains the elements of `list2` if `list1` was not empty, otherwise `list1` references the same list object as `list2` and retains its original contents
#Overall this is what the function does:The function `func_1` accepts two lists, `list1` and `list2`. If `list1` is not empty, it updates `list1` such that its last element is replaced with the entire content of `list2`. If `list1` is empty, it updates `list1` to reference the same list object as `list2`, thereby retaining the original contents of `list2`.

