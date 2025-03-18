#State of the program right berfore the function call: arr is a list of integers where each integer represents the number of stones in a pile, and the length of arr is between 1 and 2 * 10^5 inclusive.
def func_1(arr):
    A = False
    set_ = list(set(arr))
    set_.sort()
    if (set_[0] != 1) :
        return 'Alice'
        #The program returns the string 'Alice'.
    #State: *`arr` is a list of integers where each integer represents the number of stones in a pile, and the length of `arr` is between 1 and 2 * 10^5 inclusive; `A` is False; `set_` is a sorted list containing the unique elements from `arr`, and the first element of `set_` is 1
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: `A` is True; `not_c` is False; `arr` remains unchanged; `set_` remains unchanged.
    if not_c :
        A = not A
    #State: *`A` is True; `not_c` is False; `arr` remains unchanged; `set_` remains unchanged. If `not_c` is True, `A` is set to False.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice'
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers representing the number of stones in each pile, where the length of `arr` is between 1 and 2 * 10^5 inclusive. It returns 'Alice' if the smallest pile has more than 1 stone or if the differences between consecutive unique pile sizes are all exactly 1. Otherwise, it returns 'Bob'. The input list `arr` remains unchanged.

