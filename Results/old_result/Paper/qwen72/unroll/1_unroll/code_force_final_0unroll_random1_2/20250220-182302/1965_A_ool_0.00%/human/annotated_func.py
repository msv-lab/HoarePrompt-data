#State of the program right berfore the function call: arr is a list of integers where each integer represents the number of stones in a pile, and the length of arr is between 1 and 2 * 10^5.
def func_1(arr):
    A = False
    if (arr[0] != 1) :
        return 'Alice'
        #The program returns the string 'Alice'.
    #State: *`arr` is a list of integers where each integer represents the number of stones in a pile, and the length of `arr` is between 1 and 2 * 10^5; `A` is False. The first element of `arr` is 1.
    set_ = list(set(arr))
    set_.sort()
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: `A` is True, `not_c` is True.
    if not_c :
        A = not A
    #State: *`A` is True, `not_c` is True. If `not_c` is True, `A` is False and `not_c` remains True.
    return 'Alice' if A else 'Bob'
    #The program returns 'Bob'
#Overall this is what the function does:The function `func_1` accepts a list `arr` of integers where each integer represents the number of stones in a pile, and the length of `arr` is between 1 and 2 * 10^5. It returns 'Alice' if the first element of `arr` is not 1 or if the difference between any two consecutive unique elements in the sorted list of `arr` is exactly 1 and the number of such differences is odd. Otherwise, it returns 'Bob'.

