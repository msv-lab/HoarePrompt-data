#State of the program right berfore the function call: arr is a list of lists, where each inner list contains integers representing the number of stones in each pile for a test case. The length of arr is t (1 ≤ t ≤ 10^4), and for each test case, the number of piles n (1 ≤ n ≤ 2·10^5) and the number of stones in each pile a_i (1 ≤ a_i ≤ 10^9) are such that the sum of n over all test cases does not exceed 2·10^5.
def func_1(arr):
    A = False
    set_ = list(set(arr))
    set_.sort()
    if (set_[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'.
    #State: `arr` is a list of lists, where each inner list contains integers representing the number of stones in each pile for a test case. The length of `arr` is `t` (1 ≤ `t` ≤ 10^4), and for each test case, the number of piles `n` (1 ≤ `n` ≤ 2·10^5) and the number of stones in each pile `a_i` (1 ≤ `a_i` ≤ 10^9) are such that the sum of `n` over all test cases does not exceed 2·10^5. `A` is False. `set_` is a list of unique lists from `arr`, and it is now sorted in ascending order. The first element of `set_` is 1.
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: `arr` is a list of lists, `t` is the length of `arr`, `A` is the result of toggling `A` based on the number of iterations, `set_` is a list of unique lists from `arr` sorted in ascending order, the first element of `set_` is 1, `i` is the last index of `set_` that was checked. If any difference between consecutive elements in `set_` is greater than 1, `not_c` is False. Otherwise, `not_c` remains True.
    if not_c :
        A = not A
    #State: *`arr` is a list of lists, `t` is the length of `arr`, `A` is the result of toggling `A` based on the number of iterations, `set_` is a list of unique lists from `arr` sorted in ascending order, the first element of `set_` is 1, `i` is the last index of `set_` that was checked. If `not_c` is True, indicating that no difference between consecutive elements in `set_` is greater than 1, `A` is now the opposite of its previous value. Otherwise, `A` remains unchanged.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if `A` is True, otherwise it returns 'Bob'.
#Overall this is what the function does:The function `func_1` accepts a list of lists `arr`, where each inner list contains integers representing the number of stones in each pile for a test case. It returns 'Alice' if the smallest number of stones in any pile is not 1, or if the differences between consecutive unique stone counts are all exactly 1. Otherwise, it returns 'Bob'.

