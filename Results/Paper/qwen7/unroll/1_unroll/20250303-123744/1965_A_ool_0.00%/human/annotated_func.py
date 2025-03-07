#State of the program right berfore the function call: arr is a list of integers representing the initial number of stones in each pile, and the length of arr (n) satisfies 1 <= n <= 2 * 10^5. Each element in arr (a_i) satisfies 1 <= a_i <= 10^9.
def func_1(arr):
    A = False
    if (arr[0] != 1) :
        return 'Alice'
        #The program returns the string 'Alice'
    #State: `A` is False, arr[0] is 1
    set_ = list(set(arr))
    set_.sort()
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: Output State: A is True; arr[0] is 1; set_ is [1]; not_c is True.
    #
    #Explanation: The loop iterates over the elements of `set_`, which initially contains only one element [1]. Since the loop starts from index 1 and there are no more elements in `set_` to iterate over, the loop body is never executed. Therefore, the value of `A` remains `False` (initially) and then becomes `True` due to the statement `A = not A`. The values of `arr[0]` and `not_c` remain unchanged.
    if not_c :
        A = not A
    #State: `A` is True; `arr[0]` is 1; `set_` is [1]; `not_c` is False.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice'
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and always returns the string 'Alice'. This is determined by the following steps: first, it checks if the first element of `arr` is not 1, in which case it immediately returns 'Alice'. If the first element is 1, it proceeds to create a sorted list of unique elements from `arr`. It then iterates through this list to check if any two consecutive elements have a difference greater than 1. Regardless of the outcome of this check, the boolean variable `A` is toggled. Finally, based on the value of `A`, it returns 'Alice', ensuring that 'Alice' is returned in all cases.

