#State of the program right berfore the function call: arr is a list of integers representing the number of stones in each pile, where the length of the list is n (1 <= n <= 2 * 10^5) and each integer a_i satisfies 1 <= a_i <= 10^9.
def func_1(arr):
    A = False
    if (arr[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: Postcondition: `arr` is a list of integers representing the number of stones in each pile, where the length of the list is n (1 <= n <= 2 * 10^5) and each integer a_i satisfies 1 <= a_i <= 10^9; `arr[0]` equals 1.
    set_ = list(set(arr))
    set_.sort()
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: Output State: `not_c` is False, `arr` is a list of integers, `set_` is a sorted list of unique elements from `arr`.
    if not_c :
        A = not A
    #State: `not_c` is False, `arr` is a list of integers, `set_` is a sorted list of unique elements from `arr`.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' since 'not_c' is False, and 'A' is equivalent to 'not_c'.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr`, where each integer represents the number of stones in each pile, and returns either 'Alice' or 'Bob'. If the first element of `arr` is not 1, the function immediately returns 'Alice'. Otherwise, it processes the list to determine if there are any gaps greater than 1 between consecutive unique elements in the sorted list. If such gaps exist, it sets `not_c` to False. Finally, it returns 'Alice' if `not_c` is False, otherwise it returns 'Bob'.

