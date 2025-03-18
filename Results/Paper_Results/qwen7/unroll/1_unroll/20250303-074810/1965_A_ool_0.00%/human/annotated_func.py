#State of the program right berfore the function call: arr is a list of integers representing the number of stones in each pile, where the length of arr (denoted as n) satisfies 1 <= n <= 2 * 10^5 and 1 <= a_i <= 10^9 for each a_i in arr.
def func_1(arr):
    A = False
    if (arr[0] != 1) :
        return 'Alice'
        #The program returns the string 'Alice'
    #State: `A` is False, and `arr[0]` is equal to 1
    set_ = list(set(arr))
    set_.sort()
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: Output State: `A` is True, `not_c` is True, and `arr[0]` is equal to 1, `set_` is [1]
    #
    #Explanation: The loop runs from `i=1` to `len(set_)`, but since `set_` only contains one element `[1]`, the loop does not execute at all. Therefore, the value of `A` toggles once (from False to True) and `not_c` remains True. The values of `arr[0]` and `set_` remain unchanged.
    if not_c :
        A = not A
    #State: Postcondition: `A` is True, `not_c` is True, `arr[0]` is equal to 1, and `set_` is [1]. This is because the loop does not execute due to the condition `not_c` being True, so `A` toggles from its initial state of True to False and then back to True, while `not_c` remains True. The values of `arr[0]` and `set_` remain unchanged.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice'
#Overall this is what the function does:The function accepts a list of integers `arr`, representing the number of stones in each pile. It checks if the first element of `arr` is 1. If not, it returns 'Alice'. Otherwise, it processes the unique sorted elements of `arr`. If the difference between consecutive elements is never more than 1, `A` toggles once. Finally, it returns 'Alice' if `A` is True, otherwise it returns 'Bob'. The function always returns either 'Alice' or 'Bob'.

