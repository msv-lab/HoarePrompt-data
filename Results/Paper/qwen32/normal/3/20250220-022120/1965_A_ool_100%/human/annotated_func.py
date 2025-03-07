#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, followed by t pairs of lines where the first line of each pair contains an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, and the second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1(arr):
    A = False
    set_ = list(set(arr))
    set_.sort()
    if (set_[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases, followed by `t` pairs of lines where the first line of each pair contains an integer `n` (1 ≤ `n` ≤ 2·10^5) representing the number of piles, and the second line contains `n` integers `a_1, a_2, ..., a_n` (1 ≤ `a_i` ≤ 10^9) representing the number of stones in each pile; `A` is False; `set_` is a list containing unique elements from `arr` sorted in ascending order, and the first element of `set_` is 1.
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases, followed by `t` pairs of lines where the first line of each pair contains an integer `n` (1 ≤ `n` ≤ 2·10^5) representing the number of piles, and the second line contains `n` integers `a_1, a_2, ..., a_n` (1 ≤ `a_i` ≤ 10^9) representing the number of stones in each pile; `A` is `True` if the number of unique elements in `set_` is odd, otherwise `False`; `set_` is a list containing unique elements from `arr` sorted in ascending order, and the first element of `set_` is 1; `not_c` is `False` if any difference between consecutive elements in `set_` is greater than 1, otherwise `not_c` is `True`; `i` is `len(set_) - 1`.
    if not_c :
        A = not A
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases, followed by `t` pairs of lines where the first line of each pair contains an integer `n` (1 ≤ `n` ≤ 2·10^5) representing the number of piles, and the second line contains `n` integers `a_1, a_2, ..., a_n` (1 ≤ `a_i` ≤ 10^9) representing the number of stones in each pile. `A` is `False` if it was `True` and `True` if it was `False`. `set_` is a list containing unique elements from `arr` sorted in ascending order, and the first element of `set_` is 1. `not_c` is `True` if there are no differences greater than 1 between consecutive elements in `set_`. `i` is `len(set_) - 1`. If `not_c` is `True`, `A` is toggled (i.e., `A` becomes `False` if it was `True` and `True` if it was `False`).
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' or 'Bob'
#Overall this is what the function does:The function `func_1` determines the winner of a game based on the configuration of stone piles across multiple test cases. It accepts a list of integers where the first element represents the number of test cases, followed by pairs of lines for each test case: the first line contains the number of piles, and the second line contains the number of stones in each pile. The function returns 'Alice' if Alice wins and 'Bob' if Bob wins.

