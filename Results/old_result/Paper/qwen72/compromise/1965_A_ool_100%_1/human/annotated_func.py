#State of the program right berfore the function call: arr is a list of n integers (1 \le n \le 2\cdot 10^5) where each integer a_i (1 \le a_i \le 10^9) represents the initial number of stones in the i-th pile.
def func_1(arr):
    A = False
    set_ = list(set(arr))
    set_.sort()
    if (set_[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: *`arr` is a list of n integers (1 ≤ n ≤ 2·10^5) where each integer a_i (1 ≤ a_i ≤ 10^9) represents the initial number of stones in the i-th pile, `A` is False, `set_` is a sorted list containing the unique elements of `arr`, and the first element of `set_` is 1
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: `A` is True, `set_` remains a sorted list containing the unique elements of `arr`, and `not_c` is False if there is any gap greater than 1 between consecutive elements in `set_`, otherwise `not_c` remains True.
    if not_c :
        A = not A
    #State: *`A` is True, `set_` remains a sorted list containing the unique elements of `arr`. If `not_c` is True, `A` is False, and there is no gap greater than 1 between consecutive elements in `set_`. Otherwise, `not_c` remains False if there is any gap greater than 1 between consecutive elements in `set_`, and `A` remains True.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if `A` is True, otherwise it returns 'Bob'. Given the initial state, `A` is True unless `not_c` is True and there is no gap greater than 1 between consecutive elements in `set_`. If `not_c` is True, `A` becomes False. Therefore, the program returns 'Alice' if there is any gap greater than 1 between consecutive elements in `set_`, or if `not_c` is False. If `not_c` is True and there is no gap greater than 1 between consecutive elements in `set_`, the program returns 'Bob'.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and determines the winner of a game based on the properties of the numbers in `arr`. The function returns 'Alice' if the smallest number in `arr` is not 1, or if there is any gap greater than 1 between consecutive unique numbers in the sorted list of `arr`. Otherwise, it returns 'Bob' if all unique numbers in `arr` are consecutive starting from 1.

