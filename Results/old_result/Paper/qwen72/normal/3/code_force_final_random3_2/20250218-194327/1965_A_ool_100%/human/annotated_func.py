#State of the program right berfore the function call: arr is a list of integers where each integer represents the number of stones in a pile, and the length of arr is between 1 and 2 * 10^5 inclusive.
def func_1(arr):
    A = False
    set_ = list(set(arr))
    set_.sort()
    if (set_[0] != 1) :
        return 'Alice'
        #The program returns the string 'Alice'.
    #State: `arr` is a list of integers where each integer represents the number of stones in a pile, and the length of `arr` is between 1 and 2 * 10^5 inclusive; `A` is False; `set_` is a sorted list containing the unique elements from `arr`, and the first element of `set_` is 1.
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: `arr` is a list of integers where each integer represents the number of stones in a pile, and the length of `arr` is between 1 and 2 * 10^5 inclusive; `A` is the negation of the initial value of `A` if all differences between consecutive elements in `set_` are 1, otherwise `A` is the value it was last set to before the loop broke; `set_` is a sorted list containing the unique elements from `arr`, and the first element of `set_` is 1; `not_c` is False if any difference between consecutive elements in `set_` is greater than 1, otherwise `not_c` remains True; `i` is the index where the loop broke or `len(set_) - 1` if the loop completed all iterations.
    if not_c :
        A = not A
    #State: *`arr` is a list of integers where each integer represents the number of stones in a pile, and the length of `arr` is between 1 and 2 * 10^5 inclusive; `set_` is a sorted list containing the unique elements from `arr`, and the first element of `set_` is 1; if any difference between consecutive elements in `set_` is greater than 1, `not_c` is False and the program executes the if part, setting `A` to the negation of its initial value and `i` to the index where the loop broke or `len(set_) - 1` if the loop completed all iterations. Otherwise, `not_c` remains True and `A` retains the value it was last set to before the loop broke.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if `A` is True, or 'Bob' if `A` is False. `A` is the negation of its initial value if any difference between consecutive elements in `set_` is greater than 1, and retains its last set value otherwise.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` where each integer represents the number of stones in a pile, and the length of `arr` is between 1 and 2 * 10^5 inclusive. It returns 'Alice' if the smallest number in `arr` is not 1 or if there is any gap greater than 1 between consecutive unique numbers in `arr`. Otherwise, it returns 'Alice' if the number of unique elements in `arr` is odd, and 'Bob' if the number of unique elements is even.

