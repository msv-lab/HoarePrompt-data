#State of the program right berfore the function call: list1 and list2 are lists, and list1 is not empty.
def func_1(list1, list2):
    if list1 :
        list1[-1:] = list2
    else :
        list1 = list2
    #State of the program after the if-else block has been executed: *list1 and list2 are lists. Since the condition in the if statement checks if list1 is truthy (which is always the case given the precondition that list1 is not empty), the else part will never be executed. Therefore, list1 will have its last element replaced by the elements of list2, and list2 retains its status as a list.
    return list1
    #The program returns list1, which contains all its original elements except the last one, replaced by all elements of list2.
#Overall this is what the function does:The function accepts two lists, `list1` and `list2`, and returns `list1` with its last element replaced by all elements of `list2` if `list1` is not empty; if `list1` is empty, it does not modify `list1` and returns the original `list1` because the modification inside the function does not affect the original list due to scope limitations.

