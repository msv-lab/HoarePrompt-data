#State of the program right berfore the function call: arr is a list of integers representing the initial number of stones in each pile, and the length of arr (n) satisfies 1 <= n <= 2 * 10^5. Each integer in arr (a_i) satisfies 1 <= a_i <= 10^9.
def func_1(arr):
    A = False
    set_ = list(set(arr))
    set_.sort()
    if (set_[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: `set_` is a list of unique elements from `arr` sorted in ascending order, `A` is False, and the first element of `set_` is 1
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: Output State: `set_` is a list of unique elements from `arr` sorted in ascending order, `A` is either True or False (determined by the loop execution), and `not_c` is False.
    if not_c :
        A = not A
    #State: `set_` is a list of unique elements from `arr` sorted in ascending order, `A` is False, and `not_c` remains False.
    return 'Alice' if A else 'Bob'
    #The program returns 'Bob'
#Overall this is what the function does:The function accepts a list of integers `arr`, representing the initial number of stones in each pile. It first removes duplicate values from `arr` and sorts the resulting list in ascending order. If the smallest value in the sorted list is not 1, the function returns 'Alice'. Otherwise, it checks if there are any gaps greater than 1 between consecutive elements in the sorted list. Based on this check and the alternating boolean value `A`, the function finally returns either 'Alice' or 'Bob'.

