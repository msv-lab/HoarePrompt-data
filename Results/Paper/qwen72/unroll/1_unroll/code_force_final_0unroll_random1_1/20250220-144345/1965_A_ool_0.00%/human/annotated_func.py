#State of the program right berfore the function call: arr is a list of integers where each integer represents the number of stones in a pile, and the length of arr is between 1 and 2 * 10^5.
def func_1(arr):
    A = False
    if (arr[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: arr is a list of integers where each integer represents the number of stones in a pile, and the length of arr is between 1 and 2 * 10^5; A is False; the first element of arr is 1.
    set_ = list(set(arr))
    set_.sort()
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: arr is a list of integers where each integer represents the number of stones in a pile, and the length of arr is between 1 and 2 * 10^5; A is True; the first element of arr is 1; set_ is a sorted list containing the unique elements from arr; not_c is False.
    if not_c :
        A = not A
    #State: *`arr` is a list of integers where each integer represents the number of stones in a pile, and the length of `arr` is between 1 and 2 * 10^5; the first element of `arr` is 1; `set_` is a sorted list containing the unique elements from `arr`. If `not_c` is True, `A` is False and `not_c` is False. Otherwise, `A` remains True and `not_c` remains False.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if `A` is True, otherwise it returns 'Bob'. Since the initial state indicates that `A` is True when `not_c` is False, and remains True otherwise, the program will always return 'Alice'.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` where each integer represents the number of stones in a pile, and the length of `arr` is between 1 and 2 * 10^5. It returns 'Alice' if the first element of `arr` is not 1, or if the unique elements in `arr` are consecutive integers starting from 1. Otherwise, it returns 'Bob'.

