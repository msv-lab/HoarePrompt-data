#State of the program right berfore the function call: arr is a list of integers where each integer represents the number of stones in a pile, and the length of arr is between 1 and 2 * 10^5 inclusive.
def func_1(arr):
    A = False
    if (arr[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'.
    #State: `arr` is a list of integers where each integer represents the number of stones in a pile, and the length of `arr` is between 1 and 2 * 10^5 inclusive; `A` is False; the first element of `arr` is 1
    set_ = list(set(arr))
    set_.sort()
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: Output State: `arr` remains unchanged; `A` is True; `set_` remains unchanged; `not_c` is False. 
    #
    #Explanation: 
    #- The loop iterates over the indices of `set_` starting from 1.
    #- For each iteration, it checks if the difference between the current element and the previous element in `set_` is greater than 1.
    #- If the difference is greater than 1, `not_c` is set to False and the loop breaks.
    #- If the difference is not greater than 1, `A` is toggled (flipped between True and False).
    #- Since `set_` is a sorted list of unique elements from `arr` and the first element of `arr` is 1, if there is any gap greater than 1 between consecutive elements in `set_`, `not_c` will be set to False and the loop will break.
    #- If there are no gaps greater than 1, `A` will be toggled for each element in `set_` except the first one. Since `A` starts as False and is toggled an odd number of times (because the loop starts from index 1), `A` will end up as True.
    #- `arr` and `set_` remain unchanged as they are not modified within the loop.
    if not_c :
        A = not A
    #State: *`arr` remains unchanged; `A` is True if `not_c` is False, otherwise `A` is False; `set_` remains unchanged; `not_c` retains its initial value.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if `not_c` is False, otherwise it returns 'Bob'.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` representing piles of stones. It returns 'Alice' if the first element of `arr` is not 1 or if there is any gap greater than 1 between consecutive unique elements in the sorted list of `arr`. Otherwise, it returns 'Bob'. The function does not modify the input list `arr`.

