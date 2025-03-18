#State of the program right berfore the function call: arr is a list of positive integers representing the number of stones in each pile, and the length of arr is at least 1 and does not exceed 2 * 10^5.
def func_1(arr):
    A = False
    if (arr[0] != 1) :
        return 'Alice'
        #The program returns the string 'Alice'.
    #State: *`arr` is a list of positive integers representing the number of stones in each pile, and the length of `arr` is at least 1 and does not exceed 2 * 10^5; `A` is False. The first element of `arr` is 1.
    set_ = list(set(arr))
    set_.sort()
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: `arr` is a list of positive integers representing the number of stones in each pile, and the length of `arr` is at least 1 and does not exceed 2 * 10^5; `A` is either True or False depending on the final value of `i` (it toggles with each iteration); `set_` is a sorted list of unique positive integers from `arr` that must have at least 2 elements, including 1; `i` is the last index of `set_` that was processed before the loop ended; `not_c` is False if there exists any two consecutive elements in `set_` such that their difference is greater than 1, otherwise `not_c` remains True.
    if not_c :
        A = not A
    #State: *`arr` is a list of positive integers representing the number of stones in each pile, and the length of `arr` is at least 1 and does not exceed 2 * 10^5; `A` is the opposite of its previous value (if it was True, now it is False, and vice versa); `set_` is a sorted list of unique positive integers from `arr` that must have at least 2 elements, including 1; `i` is the last index of `set_` that was processed before the loop ended; `not_c` is True, indicating that there are no two consecutive elements in `set_` such that their difference is greater than 1. If `not_c` is False, the state of the variables remains unchanged.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if `A` is True, otherwise it returns 'Bob'.
#Overall this is what the function does:The function `func_1` takes a list `arr` of positive integers, where each integer represents the number of stones in each pile. The function determines the winner of a game between Alice and Bob based on the following rules: If the first pile has more than one stone, Alice wins. Otherwise, the function checks if the differences between consecutive unique values in the sorted list of piles are all exactly 1. If this condition holds, the winner alternates starting from Alice. The function returns 'Alice' if Alice wins, and 'Bob' otherwise.

