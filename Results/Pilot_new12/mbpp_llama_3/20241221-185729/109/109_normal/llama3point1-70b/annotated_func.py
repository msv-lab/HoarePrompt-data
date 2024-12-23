#State of the program right berfore the function call: list1 and list2 are lists, and list1 is not empty.
def func_1(list1, list2):
    if list1 :
        list1[-1:] = list2
    else :
        list1 = list2
    #State of the program after the if-else block has been executed: `list1` and `list2` are lists. Since the condition in the if statement is just `list1`, which is given as not empty in the precondition, the if part will always be executed when the precondition is met, meaning `list1` will have its last element replaced with the elements of `list2`. The else part, stating `list1` is equal to `list2`, will not be reached under the given precondition that `list1` is not empty. Therefore, after the execution, `list1` will be a list with its last element replaced with the elements of `list2`, and `list2` remains a list.
    return list1
    #The program returns list1, which is a list where its last element has been replaced with all elements from list2.
#Overall this is what the function does:The function accepts two parameters, `list1` and `list2`, where both are lists. If `list1` is not empty, it replaces the last element of `list1` with all elements of `list2`. If `list1` is empty, it assigns `list2` to `list1`. The function returns the modified `list1`, which is a list where its last element has been replaced with all elements of `list2` if `list1` was not empty, or is equal to `list2` if `list1` was empty. The function modifies the original `list1` in-place if it is not empty. The state of `list2` remains unchanged.

