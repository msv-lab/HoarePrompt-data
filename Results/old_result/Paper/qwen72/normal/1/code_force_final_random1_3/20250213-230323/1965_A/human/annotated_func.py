#State of the program right berfore the function call: arr is a list of positive integers representing the number of stones in each pile, and the length of arr is between 1 and 2 * 10^5 inclusive.
def func_1(arr):
    A = False
    if (arr[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'.
    #State: *`arr` is a list of positive integers representing the number of stones in each pile, and the length of `arr` is between 1 and 2 * 10^5 inclusive; `A` is `False`. The first element of `arr` is 1.
    set_ = list(set(arr))
    set_.sort()
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: `arr` is a list of positive integers representing the number of stones in each pile, and the length of `arr` is between 1 and 2 * 10^5 inclusive; `A` is `True` if the loop completes without breaking, otherwise it is `False`; `set_` is a sorted list containing the unique elements from `arr`, including the number 1; `not_c` is `False` if any two consecutive elements in `set_` have a difference greater than 1, otherwise it remains `True`.
    if not_c :
        A = not A
    #State: *`arr` is a list of positive integers representing the number of stones in each pile, and the length of `arr` is between 1 and 2 * 10^5 inclusive; `A` is `False` if the loop completes without breaking, otherwise it is `True`; `set_` is a sorted list containing the unique elements from `arr`, including the number 1; `not_c` is `True` if no two consecutive elements in `set_` have a difference greater than 1. If `not_c` is `True`, then `A` is `False` if the loop completes without breaking, otherwise `A` is `True`.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if `A` is `True`, otherwise it returns 'Bob'. Here, `A` is `True` if the loop breaks before completing, indicating a condition was met that changed `A` to `True`. If the loop completes without breaking, `A` remains `False`. Additionally, if `not_c` is `True`, meaning no two consecutive elements in `set_` have a difference greater than 1, then `A` is `False` unless the loop breaks.
#Overall this is what the function does:The function `func_1` takes a list `arr` of positive integers as input, where the length of `arr` is between 1 and 2 * 10^5 inclusive. It returns 'Alice' if the first element of `arr` is not 1. If the first element is 1, the function checks if the differences between consecutive unique elements in `arr` are all 1. If any difference is greater than 1, the function returns 'Alice' if the loop breaks early, otherwise it returns 'Bob'. If all differences are exactly 1, the function returns 'Bob' unless the loop breaks early, in which case it returns 'Alice'.

