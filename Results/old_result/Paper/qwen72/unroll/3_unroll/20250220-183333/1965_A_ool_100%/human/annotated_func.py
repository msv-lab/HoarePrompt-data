#State of the program right berfore the function call: arr is a list of positive integers where 1 <= len(arr) <= 2 * 10^5, and each element a_i in arr satisfies 1 <= a_i <= 10^9.
def func_1(arr):
    A = False
    set_ = list(set(arr))
    set_.sort()
    if (set_[0] != 1) :
        return 'Alice'
        #The program returns the string 'Alice'.
    #State: *`arr` is a list of positive integers where 1 <= len(arr) <= 2 * 10^5, and each element a_i in `arr` satisfies 1 <= a_i <= 10^9; `A` is False; `set_` is a sorted list containing the unique elements from `arr`, and the first element of `set_` is 1
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: Output State: `A` is True; `not_c` is False; `set_` remains a sorted list containing the unique elements from `arr`, and the first element of `set_` is 1.
    if not_c :
        A = not A
    #State: *`A` is True; `not_c` is False; `set_` remains a sorted list containing the unique elements from `arr`, and the first element of `set_` is 1. If `not_c` is True, `A` is False.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice'
#Overall this is what the function does:The function `func_1` accepts a list `arr` of positive integers. It checks if the list contains all consecutive integers starting from 1. If the list does not contain all consecutive integers starting from 1, or if the smallest integer is not 1, the function returns 'Alice'. If the list contains all consecutive integers starting from 1, the function returns 'Bob'.

