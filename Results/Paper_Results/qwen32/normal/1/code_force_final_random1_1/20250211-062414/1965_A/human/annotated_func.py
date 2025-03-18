#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, followed by pairs of lines for each test case: the first line contains an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, and the second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1(arr):
    A = False
    if (arr[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases, followed by pairs of lines for each test case: the first line contains an integer `n` (1 ≤ `n` ≤ 2·10^5) representing the number of piles, and the second line contains `n` integers `a_1, a_2, ..., a_n` (1 ≤ `a_i` ≤ 10^9) representing the number of stones in each pile. The sum of `n` over all test cases does not exceed 2·10^5; `A` is False. Additionally, the first element of `arr` is 1.
    set_ = list(set(arr))
    set_.sort()
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: `A` is `True` or `False` based on the number of iterations, `not_c` is `True` if no gaps greater than 1 exist in `set_`, otherwise `False`, and `i` is the last index checked or where the loop broke.
    if not_c :
        A = not A
    #State: `A` is flipped (if `A` was `True`, it becomes `False`; if `A` was `False`, it becomes `True`). `not_c` is `True`, indicating no gaps greater than 1 exist in `set_`. `i` is the last index checked or where the loop broke.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if A is True, otherwise it returns 'Bob'.
#Overall this is what the function does:The function `func_1` determines the winner of a game based on the configuration of stone piles across multiple test cases. It accepts a list of integers where the first element indicates the number of test cases, followed by pairs of lines for each test case: the first line specifies the number of piles, and the second line lists the number of stones in each pile. The function returns 'Alice' if a specific condition related to the uniqueness and sequentiality of stone counts is met, otherwise it returns 'Bob'.

