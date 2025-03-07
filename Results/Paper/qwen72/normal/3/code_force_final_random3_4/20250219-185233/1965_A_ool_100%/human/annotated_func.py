#State of the program right berfore the function call: arr is a list of integers where each integer represents the number of stones in a pile, and the length of arr is between 1 and 2 * 10^5.
def func_1(arr):
    A = False
    set_ = list(set(arr))
    set_.sort()
    if (set_[0] != 1) :
        return 'Alice'
        #The program returns the string 'Alice'.
    #State: `arr` is a list of integers where each integer represents the number of stones in a pile, and the length of `arr` is between 1 and 2 * 10^5; `A` is False; `set_` is a sorted list containing the unique elements from `arr` in ascending order, and the first element of `set_` is 1.
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: `arr` is a list of integers where each integer represents the number of stones in a pile, and the length of `arr` is between 1 and 2 * 10^5; `A` is either True or False depending on the number of iterations and whether the loop was broken; `set_` is a sorted list containing the unique elements from `arr` in ascending order, and the first element of `set_` is 1; `not_c` is False if any two consecutive elements in `set_` have a difference greater than 1, otherwise `not_c` is True; `i` is the last index of `set_` that was checked, which could be less than `len(set_) - 1` if the loop was broken, or `len(set_) - 1` if the loop completed all iterations.
    if not_c :
        A = not A
    #State: *`arr` is a list of integers where each integer represents the number of stones in a pile, and the length of `arr` is between 1 and 2 * 10^5; `A` is either the opposite of its previous value if `not_c` is True, or remains unchanged if `not_c` is False; `set_` is a sorted list containing the unique elements from `arr` in ascending order, and the first element of `set_` is 1; `not_c` is True if no two consecutive elements in `set_` have a difference greater than 1, otherwise it is False; `i` is the last index of `set_` that was checked, which could be less than `len(set_) - 1` if the loop was broken, or `len(set_) - 1` if the loop completed all iterations.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if `A` is True, otherwise it returns 'Bob'. `A` is either the opposite of its previous value if `not_c` is True, or remains unchanged if `not_c` is False. `not_c` is True if no two consecutive elements in `set_` have a difference greater than 1, otherwise it is False.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` where each integer represents the number of stones in a pile, and the length of `arr` is between 1 and 2 * 10^5. The function determines the winner of a game based on the unique values in `arr` and their differences. If the smallest unique value in `arr` is not 1, the function returns 'Alice'. Otherwise, it checks if the differences between consecutive unique values are all 1. If they are, the function toggles the value of `A` an even number of times, resulting in `A` being False, and returns 'Bob'. If any difference is greater than 1, `A` is toggled an odd number of times, resulting in `A` being True, and the function returns 'Alice'.

