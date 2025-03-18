#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, and for each test case, the list contains an integer n (1 ≤ n ≤ 2·10^5) followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1(arr):
    A = False
    if (arr[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases, and for each test case, the list contains an integer `n` (1 ≤ `n` ≤ 2·10^5) followed by `n` integers `a_1, a_2, ..., a_n` (1 ≤ `a_i` ≤ 10^9) representing the initial number of stones in each pile. The sum of `n` over all test cases does not exceed 2·10^5; `A` is `False`. Additionally, the first element `t` of `arr` is equal to 1.
    set_ = list(set(arr))
    set_.sort()
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: `A` is either `True` or `False` depending on the number of iterations where the difference between consecutive elements in `set_` is 1 or less, and `not_c` is `False` if any difference is greater than 1, otherwise `True`.
    if not_c :
        A = not A
    #State: `A` is `False` if it was `True` and `True` if it was `False`, and `not_c` remains `True`. If `not_c` was `False`, then `A` remains unchanged and `not_c` remains `False`.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if A is True, otherwise it returns 'Bob'
#Overall this is what the function does:The function `func_1` determines the winner of a game based on the configuration of stone piles provided in the input list `arr`. The list starts with the number of test cases, and for each test case, it contains the number of piles followed by the number of stones in each pile. The function returns 'Alice' if a specific condition related to the differences between the sorted unique stone counts is met, otherwise it returns 'Bob'.

