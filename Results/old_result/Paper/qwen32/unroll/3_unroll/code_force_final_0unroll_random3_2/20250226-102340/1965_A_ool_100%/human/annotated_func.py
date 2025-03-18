#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, and the following elements are pairs of integers. For each test case, the first integer n (1 ≤ n ≤ 2·10^5) represents the number of piles, and the next n integers (1 ≤ a_i ≤ 10^9) represent the number of stones in each pile. The total number of piles across all test cases does not exceed 2·10^5.
def func_1(arr):
    A = False
    set_ = list(set(arr))
    set_.sort()
    if (set_[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases, and the following elements are pairs of integers. For each test case, the first integer `n` (1 ≤ `n` ≤ 2·10^5) represents the number of piles, and the next `n` integers (1 ≤ `a_i` ≤ 10^9) represent the number of stones in each pile. The total number of piles across all test cases does not exceed 2·10^5; `A` is `False`; `set_` is a sorted list of unique integers from `arr`. The smallest element in `set_` is 1.
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases, and the following elements are pairs of integers. For each test case, the first integer `n` (1 ≤ `n` ≤ 2·10^5) represents the number of piles, and the next `n` integers (1 ≤ `a_i` ≤ 10^9) represent the number of stones in each pile. The total number of piles across all test cases does not exceed 2·10^5; `A` is `True` if `len(set_) - 1` is odd, otherwise `False`; `set_` is a sorted list of unique integers from `arr`. The smallest element in `set_` is 1; `not_c` is `False` if there is any pair of consecutive elements in `set_` with a difference greater than 1, otherwise `True`.
    if not_c :
        A = not A
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases, and the following elements are pairs of integers. For each test case, the first integer `n` (1 ≤ `n` ≤ 2·10^5) represents the number of piles, and the next `n` integers (1 ≤ `a_i` ≤ 10^9) represent the number of stones in each pile. The total number of piles across all test cases does not exceed 2·10^5. `A` is `False` if `len(set_) - 1` is odd, otherwise `True`. `set_` is a sorted list of unique integers from `arr`. The smallest element in `set_` is 1. If `not_c` is `True`, indicating there are no pairs of consecutive elements in `set_` with a difference greater than 1, then `A` is `False` if the number of unique elements minus one is odd, otherwise `A` is `True`. If `not_c` is `False`, `A` remains unchanged.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if A is True, otherwise it returns 'Bob'.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` where the first element `t` represents the number of test cases. For each test case, the first integer `n` represents the number of piles, and the following `n` integers represent the number of stones in each pile. The function determines the winner of a game based on the unique stone counts across all test cases. If the smallest unique stone count is not 1, or if there are any gaps greater than 1 between consecutive unique stone counts, the function returns 'Alice'. Otherwise, it returns 'Alice' if the number of unique stone counts minus one is even, and 'Bob' if it is odd.

