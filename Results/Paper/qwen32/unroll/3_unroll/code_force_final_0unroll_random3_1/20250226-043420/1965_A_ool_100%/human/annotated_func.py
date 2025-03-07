#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, and for each test case, the first element n (1 ≤ n ≤ 2·10^5) is followed by n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1(arr):
    A = False
    set_ = list(set(arr))
    set_.sort()
    if (set_[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases, and for each test case, the first element `n` (1 ≤ `n` ≤ 2·10^5) is followed by `n` integers `a_1, a_2, ..., a_n` (1 ≤ `a_i` ≤ 10^9) representing the initial number of stones in each pile; `A` is False; `set_` is a sorted list of unique integers from `arr`. The first element of `set_` is 1.
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: A is True if the number of elements in set_ minus 1 is odd, otherwise False; not_c is False if any consecutive elements in set_ have a difference greater than 1, otherwise True.
    if not_c :
        A = not A
    #State: `A` is True if the number of elements in `set_` minus 1 is even, otherwise `A` is False; `not_c` is True. If `not_c` is False, the postcondition of the else part is not specified and thus does not affect the overall postcondition.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if the number of elements in `set_` minus 1 is even, otherwise it returns 'Bob'
#Overall this is what the function does:The function `func_1` accepts a list of integers where the first element represents the number of test cases. Each test case starts with an integer `n` followed by `n` integers representing the initial number of stones in each pile. The function determines the winner of a game based on the uniqueness and consecutive nature of the stone counts. It returns 'Alice' if the number of unique stone counts minus one is even, otherwise it returns 'Bob'.

