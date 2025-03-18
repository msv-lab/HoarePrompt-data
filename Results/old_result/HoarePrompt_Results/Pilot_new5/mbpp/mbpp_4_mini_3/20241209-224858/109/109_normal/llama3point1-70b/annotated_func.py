#State of the program right berfore the function call: list1 and list2 are both lists, and list1 is non-empty.
def func_1(list1, list2):
    if list1 :
        list1[-1:] = list2
    else :
        list1 = list2
    #State of the program after the if-else block has been executed: *`list1` is a non-empty list. If `list1` is modified by replacing its last element with `list2`, then `list2` is a list. If `list1` is empty, then `list2` is also empty.
    return list1
    #The program returns list1, which is a non-empty list. If list1 is modified, it contains all elements except for the last element that has been replaced by list2, which is also a list.
#Overall this is what the function does:The function accepts two lists, `list1` (which is non-empty) and `list2`. It replaces the last element of `list1` with the contents of `list2`. If `list1` is empty (though the precondition states it is non-empty), it would instead assign `list2` to `list1`. The function returns `list1`, which will either have its last element replaced by `list2` or remain unchanged with `list2` assigned to it if it were empty. However, since `list1` is guaranteed to be non-empty, the only applicable behavior is replacing the last element with `list2`.

