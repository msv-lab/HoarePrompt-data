#State of the program right berfore the function call: arr is a list of integers where each integer represents the number of stones in a pile, and the length of arr is between 1 and 2 * 10^5.
def func_1(arr):
    A = False
    set_ = list(set(arr))
    set_.sort()
    if (set_[0] != 1) :
        return 'Alice'
        #The program returns the string 'Alice'.
    #State: *`arr` is a list of integers where each integer represents the number of stones in a pile, and the length of `arr` is between 1 and 2 * 10^5, `A` is False, `set_` is a sorted list containing the unique elements from `arr` in ascending order, and the first element of `set_` is 1
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: Output State: `A` is True, `not_c` is True, `set_` remains a sorted list containing the unique elements from `arr` in ascending order, and the first element of `set_` is 1.
    if not_c :
        A = not A
    #State: `A` is True, `not_c` is True, `set_` remains a sorted list containing the unique elements from `arr` in ascending order, and the first element of `set_` is 1. If `not_c` is True, then `A` is False.
    return 'Alice' if A else 'Bob'
    #The program returns 'Bob'
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers, where each integer represents the number of stones in a pile, and the length of `arr` is between 1 and 2 * 10^5. It returns 'Alice' if the smallest pile has more than 1 stone or if the differences between consecutive unique pile sizes are all 1. Otherwise, it returns 'Bob'.

