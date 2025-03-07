#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, followed by t pairs of lines where the first line of each pair contains a single integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, and the second line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1(arr):
    A = False
    if (arr[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases, followed by `t` pairs of lines where the first line of each pair contains a single integer `n` (1 ≤ `n` ≤ 2·10^5) representing the number of piles, and the second line contains `n` integers `a_1, a_2, ..., a_n` (1 ≤ `a_i` ≤ 10^9) representing the initial number of stones in each pile. The sum of `n` over all test cases does not exceed 2·10^5; `A` is `False`. Additionally, the first element `t` of `arr` is equal to 1.
    set_ = list(set(arr))
    set_.sort()
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: A is determined by the parity of the number of consecutive elements in set_; not_c is False if any consecutive elements in set_ have a difference greater than 1, otherwise True.
    if not_c :
        A = not A
    #State: A is the opposite of its initial value if not_c is True, meaning no consecutive elements in set_ have a difference greater than 1. If not_c is False, A remains unchanged.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if A is True, otherwise 'Bob'
#Overall this is what the function does:The function `func_1` determines the winner of a game based on the input list `arr`. The list `arr` starts with an integer `t` representing the number of test cases. For each test case, there is an integer `n` followed by `n` integers representing the number of stones in each pile. The function returns 'Alice' if the first element `t` is not equal to 1, or if a specific condition related to the uniqueness and consecutive nature of the stone counts is met. Otherwise, it returns 'Bob'.

