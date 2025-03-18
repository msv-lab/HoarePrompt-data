#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, followed by pairs of lines for each test case. Each pair starts with an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, and the next line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1(arr):
    A = False
    if (arr[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases, followed by pairs of lines for each test case. Each pair starts with an integer `n` (1 ≤ `n` ≤ 2·10^5) representing the number of piles, and the next line contains `n` integers `a_1, a_2, ..., a_n` (1 ≤ `a_i` ≤ 10^9) representing the number of stones in each pile. The sum of `n` over all test cases does not exceed 2·10^5; `A` is False. Additionally, the first element of `arr` is equal to 1.
    set_ = list(set(arr))
    set_.sort()
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: `arr` is unchanged, `A` is either `True` or `False` depending on the number of iterations, `set_` is the sorted version of `arr`, `not_c` is `True` if no difference greater than 1 was found, otherwise `False`.
    if not_c :
        A = not A
    #State: `arr` is unchanged, `A` is toggled (i.e., `False` if it was `True` or `True` if it was `False`), `set_` is the sorted version of `arr`, and `not_c` is `True`. No difference greater than 1 was found in `arr`.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if A is True, otherwise it returns 'Bob'.
#Overall this is what the function does:The function `func_1` takes a list of integers `arr` as input, where the first element `t` indicates the number of test cases. Each test case consists of an integer `n` followed by `n` integers representing the number of stones in each pile. The function determines the winner of a game based on the conditions described in the code and returns 'Alice' or 'Bob'. Specifically, it returns 'Alice' if the first element of `arr` is not 1, or if a certain condition involving the sorted unique elements of `arr` is met; otherwise, it returns 'Bob'.

