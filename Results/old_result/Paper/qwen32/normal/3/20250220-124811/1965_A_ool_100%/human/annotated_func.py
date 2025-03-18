#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, and for each test case, the list contains an integer n (1 ≤ n ≤ 2·10^5) followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1(arr):
    A = False
    set_ = list(set(arr))
    set_.sort()
    if (set_[0] != 1) :
        return 'Alice'
        #The program returns the string 'Alice'
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases, and for each test case, the list contains an integer `n` (1 ≤ `n` ≤ 2·10^5) followed by `n` integers `a_1, a_2, ..., a_n` (1 ≤ `a_i` ≤ 10^9) representing the initial number of stones in each pile; `A` is `False`; `set_` is a list of unique elements from `arr` in ascending order, and the first element of `set_` is 1.
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: - If `not_c` remains `True` after all iterations, it means there were no gaps greater than 1 between consecutive elements in `set_`. In this case, `A` will be `True` if the number of iterations (excluding the first element) is odd, and `False` if it is even.
    #- If `not_c` becomes `False` at any point during the loop, the loop breaks, and `A` will be `True` if the number of completed iterations (excluding the first element) is odd, and `False` if it is even.
    #
    #Given the information and the pattern observed, the final output state can be described as follows:
    #
    #If the loop completes all iterations without setting `not_c` to `False`, `A` will be `True` if the number of unique elements in `set_` (excluding the first element) is odd, and `False` if it is even. `not_c` will be `True`.
    #
    #If the loop breaks due to finding a gap greater than 1, `not_c` will be `False`, and `A` will be `True` if the number of completed iterations (excluding the first element) is odd, and `False` if it is even.
    #
    #Since the exact number of unique elements in `set_` is not provided, we will assume the loop completes all iterations without breaking. Therefore, the final output state is:
    #
    #Output State:
    if not_c :
        A = not A
    #State: `not_c` is a boolean. If `not_c` is `True`, then the value of `A` is flipped (i.e., if `A` was `True`, it becomes `False`, and if `A` was `False`, it becomes `True`). If `not_c` is `False`, the value of `A` remains unchanged.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' or 'Bob' based on the value of A after it may have been flipped by not_c.
#Overall this is what the function does:The function `func_1` takes a list of integers as input, where the first element represents the number of test cases. For each test case, the list contains an integer `n` followed by `n` integers representing the initial number of stones in each pile. The function determines the winner of a game based on the unique stone counts across all test cases. If the smallest unique stone count is not 1, it returns 'Alice'. Otherwise, it checks for gaps greater than 1 between consecutive unique stone counts. If no such gaps exist, it alternates the winner based on the count of unique stone counts (excluding the first element). If gaps exist, it alternates the winner based on the number of completed iterations. The final output is either 'Alice' or 'Bob'.

