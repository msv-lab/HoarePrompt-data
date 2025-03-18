#State of the program right berfore the function call: arr is a list of integers representing the number of stones in each pile, where the length of arr (n) satisfies 1 <= n <= 2 * 10^5 and each element a_i in arr satisfies 1 <= a_i <= 10^9.
def func_1(arr):
    A = False
    if (arr[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: `A` is False, arr[0] is 1
    set_ = list(set(arr))
    set_.sort()
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: Output State: `A` is True, `arr[0]` is 1, `set_` contains at least two elements including 1 and 2, `not_c` is False.
    #
    #Explanation: The loop runs until the condition `set_[i] - set_[i - 1] > 1` is met, which happens on the second iteration with `set_` containing at least two elements including 1 and 2. After the second iteration, the loop breaks because the condition is satisfied, making `not_c` False. Since the loop variable `A` is toggled (`not A`) in each iteration and it starts as `False`, after the second iteration (and thus three total iterations), `A` becomes `True`. The value of `arr[0]` remains unchanged at 1, and `set_` must include at least 1 and 2. The value of `not_c` remains False as the loop breaks when the condition is met.
    if not_c :
        A = not A
    #State: `A` is True, `arr[0]` is 1, `set_` contains at least two elements including 1 and 2, `not_c` is False.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice'
#Overall this is what the function does:The function accepts a list of integers `arr` representing the number of stones in each pile. It first checks if the first element of `arr` is not 1, in which case it returns 'Alice'. Otherwise, it creates a sorted list of unique elements from `arr`, then iterates through this list to check if any two consecutive elements have a difference greater than 1. If such a pair is found, it sets `not_c` to False and breaks out of the loop. The boolean variable `A` is toggled in each iteration. Finally, it returns 'Alice' if `A` is True, otherwise it returns 'Bob'. In all cases, the function returns either 'Alice' or 'Bob'.

