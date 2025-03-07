#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases. Each test case is represented by two subsequent elements: an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1(arr):
    A = False
    if (arr[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: `arr` is a list of integers where the first element `t` (1 ≤ `t` ≤ 10^4) represents the number of test cases. Each test case is represented by two subsequent elements: an integer `n` (1 ≤ `n` ≤ 2·10^5) representing the number of piles, and a list of `n` integers `a_1, a_2, ..., a_n` (1 ≤ `a_i` ≤ 10^9) representing the initial number of stones in each pile. The sum of `n` over all test cases does not exceed 2·10^5. Additionally, `arr[0]` is equal to 1. `A` is `False`.
    set_ = list(set(arr))
    set_.sort()
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: - `A` will be either `True` or `False` depending on the number of times it was toggled.
    #   - `not_c` will be `False` if any difference between consecutive elements in `set_` is greater than 1, otherwise, it will be `True`.
    #   - The values of `arr`, `t`, `n`, and the list of integers `a_1, a_2, ..., a_n` will remain unchanged.
    #
    #Given that `arr[0]` is `1`, this means there is only one test case. The list `set_` will contain the unique elements from `arr`, which includes `1`, `n`, and the integers `a_1, a_2, ..., a_n`.
    #
    #Since `arr[0]` is `1`, and assuming there is only one test case, `set_` will be `[1, n, a_1, a_2, ..., a_n]` sorted. The loop will iterate over this sorted list and check the differences between consecutive elements.
    #
    #Let's consider the output state in a general format:
    #
    #- If the differences between consecutive elements in `set_` are all ≤ 1, `not_c` will remain `True` and `A` will be toggled based on the number of elements.
    #- If any difference is > 1, `not_c` will be `False` and the loop will break.
    #
    #Since the exact values of `n` and `a_1, a_2, ..., a_n` are not specified, we can't determine the exact value of `A`. However, we can determine the state of `not_c`.
    #
    #Output State:
    if not_c :
        A = not A
    #State: `A` is the opposite of its initial value if `not_c` is `True`; otherwise, `A` remains unchanged. `not_c` is `True` if the differences between consecutive elements in `set_` are all ≤ 1, otherwise `not_c` is `False`. The values of `arr`, `t`, `n`, and the list of integers `a_1, a_2, ..., a_n` remain unchanged.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if the final value of `A` is True, otherwise it returns 'Bob'.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` where the first element `t` represents the number of test cases. Each test case is defined by an integer `n` (number of piles) followed by `n` integers (initial number of stones in each pile). The function returns 'Alice' if the first element `t` is not equal to 1, or if a specific condition based on the uniqueness and consecutive differences of elements in the test case is met. Otherwise, it returns 'Bob'.

