#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, followed by t test cases. Each test case consists of an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1(arr):
    A = False
    set_ = list(set(arr))
    set_.sort()
    if (set_[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases, followed by `t` test cases. Each test case consists of an integer `n` (1 ≤ `n` ≤ 2·10^5) representing the number of piles, followed by `n` integers `a_1, a_2, ..., a_n` (1 ≤ `a_i` ≤ 10^9) representing the initial number of stones in each pile. The sum of `n` over all test cases does not exceed 2·10^5; `A` is False; `set_` is a sorted list of unique integers from `arr`. The first element of `set_` is 1.
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases, followed by `t` test cases. Each test case consists of an integer `n` (1 ≤ `n` ≤ 2·10^5) representing the number of piles, followed by `n` integers `a_1, a_2, ..., a_n` (1 ≤ `a_i` ≤ 10^9) representing the initial number of stones in each pile. The sum of `n` over all test cases does not exceed 2·10^5; `A` is True if the number of iterations is odd and the loop does not break early, otherwise `A` is False; `set_` is a sorted list of unique integers from `arr` with the first element being 1; `not_c` is False if any difference between consecutive elements in `set_` is greater than 1, otherwise `not_c` is True; `i` is `len(set_) - 1` unless the loop breaks early.
    if not_c :
        A = not A
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases, followed by `t` test cases. Each test case consists of an integer `n` (1 ≤ `n` ≤ 2·10^5) representing the number of piles, followed by `n` integers `a_1, a_2, ..., a_n` (1 ≤ `a_i` ≤ 10^9) representing the initial number of stones in each pile. The sum of `n` over all test cases does not exceed 2·10^5. `A` is False if it was True, and True if it was False, provided `not_c` is True. `set_` is a sorted list of unique integers from `arr` with the first element being 1. `not_c` is True if no difference between consecutive elements in `set_` is greater than 1. `i` is `len(set_) - 1` unless the loop breaks early. If `not_c` is False, the values of `A`, `set_`, `not_c`, and `i` remain unchanged.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if A is True, otherwise it returns 'Bob'.
#Overall this is what the function does:The function `func_1` takes a list of integers as input, where the first element indicates the number of test cases, and each subsequent test case consists of an integer representing the number of piles followed by the number of stones in each pile. The function returns 'Alice' if a specific condition is met, otherwise it returns 'Bob'. The condition is determined based on the uniqueness and consecutive nature of the stone counts across all test cases.

