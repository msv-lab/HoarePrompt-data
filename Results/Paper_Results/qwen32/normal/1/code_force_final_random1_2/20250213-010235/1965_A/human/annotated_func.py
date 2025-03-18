#State of the program right berfore the function call: arr is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, followed by pairs of lines for each test case. Each pair starts with an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, and the next line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5.
def func_1(arr):
    A = False
    if (arr[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: arr is a list of integers where the first element t (1 ≤ t ≤ 10^4) represents the number of test cases, followed by pairs of lines for each test case. Each pair starts with an integer n (1 ≤ n ≤ 2·10^5) representing the number of piles, and the next line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the initial number of stones in each pile. The sum of n over all test cases does not exceed 2·10^5; A is False. Additionally, the first element of arr (t) is equal to 1.
    set_ = list(set(arr))
    set_.sort()
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: arr is a sorted list of integers with at least two elements where the first element t is 1, followed by a unique set of integers representing the number of piles n and the initial number of stones in each pile without duplicates; A is False; not_c is True.
    if not_c :
        A = not A
    #State: arr is a sorted list of integers with at least two elements where the first element t is 1, followed by a unique set of integers representing the number of piles n and the initial number of stones in each pile without duplicates. If the current value of not_c is True, then A is True and not_c remains True. Otherwise, A remains False and not_c remains False.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if not_c is True, otherwise it returns 'Bob'.
#Overall this is what the function does:The function `func_1` takes a list of integers as input, where the first element indicates the number of test cases. For each test case, it determines the winner of a game based on specific conditions related to the number of piles and the number of stones in each pile. The function returns 'Alice' if the conditions for winning are met according to the logic within the function; otherwise, it returns 'Bob'.

