#State of the program right berfore the function call: arr is a list of integers representing the number of stones in each pile, and the length of arr (n) satisfies 1 <= n <= 2 * 10^5. Each integer in the list represents the initial number of stones in a pile and satisfies 1 <= a_i <= 10^9.
def func_1(arr):
    A = False
    set_ = list(set(arr))
    set_.sort()
    if (set_[0] != 1) :
        return 'Alice'
        #The program returns 'Alice'
    #State: `A` is False, `set_` is a list of unique elements from `arr` sorted in ascending order, and the first element of `set_` is 1
    not_c = True
    for i in range(1, len(set_)):
        if set_[i] - set_[i - 1] > 1:
            not_c = False
            break
        
        A = not A
        
    #State: Output State: `A` is True, `not_c` is False, `set_` is a list of unique elements from `arr` sorted in ascending order, and the first element of `set_` is 1.
    #
    #Explanation: The loop iterates through the elements of `set_` starting from the second element. If the difference between consecutive elements is greater than 1, `not_c` is set to False and the loop breaks. Otherwise, `A` toggles between True and False with each iteration. Since the loop starts from `i=1`, it will check the difference between each pair of consecutive elements (i and i-1). If no such pair exists where the difference is greater than 1, `not_c` remains True, but since the loop will eventually break when the condition is met, `not_c` becomes False. The value of `A` will be True if the number of iterations is even, and False if it's odd. Given the loop starts from `i=1` and goes up to `len(set_) - 1`, the number of iterations is always one less than the length of `set_`, which means `A` will be True if the length of `set_` is even, and False if it's odd. However, without knowing the exact length of `set_`, we can only definitively say that `not_c` will be False if the condition `set_[i] - set_[i - 1] > 1` is ever met during the loop.
    if not_c :
        A = not A
    #State: `A` is True if the length of `set_` is even, and False if it's odd. `not_c` is False if the difference between any two consecutive elements in `set_` is greater than 1. Otherwise, `not_c` remains True.
    return 'Alice' if A else 'Bob'
    #The program returns 'Alice' if the length of set_ is even, and 'Bob' if it's odd.
#Overall this is what the function does:The function accepts a list of integers representing the number of stones in each pile. It first removes duplicates and sorts the list. Then, it checks if the smallest number is 1. If not, it returns 'Alice'. Next, it iterates through the sorted unique elements to determine if the difference between any two consecutive elements is greater than 1. If such a difference is found, it sets a flag to False and breaks the loop. After the loop, it toggles a boolean value based on the length of the unique elements list. Finally, it returns 'Alice' if the length of the unique elements list is even, otherwise it returns 'Bob'.

