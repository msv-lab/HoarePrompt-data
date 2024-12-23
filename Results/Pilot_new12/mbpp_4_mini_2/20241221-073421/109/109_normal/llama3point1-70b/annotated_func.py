#State of the program right berfore the function call: list1 and list2 are both lists. list1 must have at least one element so that its last element can be replaced.
def func_1(list1, list2):
    if list1 :
        list1[-1:] = list2
    else :
        list1 = list2
    #State of the program after the if-else block has been executed: *`list1` and `list2` are both lists. If `list1` is not empty, it will contain its original elements up to the second-to-last element, followed by all elements of `list2`, while `list2` remains unchanged. If `list1` is empty, `list1` is now the same as `list2`.
    return list1
    #The program returns list1, which either contains its original elements up to the second-to-last element followed by all elements of list2, or is the same as list2 if list1 is empty.
#Overall this is what the function does:The function accepts two lists, `list1` and `list2`. It checks if `list1` is non-empty. If so, it replaces the last element of `list1` with all elements from `list2`, effectively extending `list1` to include the elements of `list2` after removing its last element. If `list1` is empty, it assigns `list2` to `list1`. The function then returns the modified `list1`. Notably, if `list1` has only one element, that element is completely replaced by the contents of `list2`. The function does not directly modify `list2`, maintaining its original state throughout the operation. Additionally, edge cases such as `list1` being empty or containing only one element are properly handled. If `list1` is initially empty, it directly becomes equal to `list2` upon return.

