#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, followed by t pairs of lines where the first line of each pair contains an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, and the second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1(arr):
    A = False
    set_ = list(set(arr))
    set_.sort()
    if (set_[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: `arr` is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, followed by t pairs of lines where the first line of each pair contains an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, and the second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile; `set_` is a sorted list containing unique elements from `arr`; `A` is False; the first element of `set_` is 1.
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: `arr` is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, followed by t pairs of lines where the first line of each pair contains an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, and the second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile; `set_` is a sorted list containing unique elements from `arr`; `A` is True if the number of elements in `set_` (excluding the first element) is odd, otherwise False; `not_c` is True if all elements in `set_` are consecutive, otherwise False.
    if not_c :
        A = not A
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases, followed by `t` pairs of lines where the first line of each pair contains an integer `n` (1 ≤ `n` ≤ 2·10^5) representing the number of piles, and the second line contains `n` integers `a_1, a_2, ..., a_n` (1 ≤ `a_i` ≤ 10^9) representing the initial number of stones in each pile; `set_` is a sorted list containing unique elements from `arr`; `A` is False if the number of elements in `set_` (excluding the first element) is odd, otherwise True; `not_c` is True if all elements in `set_` are consecutive, otherwise False. If `not_c` is True, then `A` is set to the negation of its original value.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if the final value of A is True, otherwise it returns 'Bob'
#Overall this is what the function does:The function `func_1` determines the winner of a game based on the configuration of stone piles across multiple test cases. It accepts a list `arr` where the first element is the number of test cases, followed by pairs of lines for each test case: the first line specifies the number of piles, and the second line specifies the number of stones in each pile. The function returns 'Alice' if a specific condition related to the uniqueness and consecutiveness of stone counts is met, otherwise it returns 'Bob'.

