#State of the program right berfore the function call: arr is a list of integers representing the initial number of stones in each pile, and the length of arr (n) satisfies 1 <= n <= 2 * 10^5. Each integer in the list satisfies 1 <= a_i <= 10^9.
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
        
    #State: Output State: `A` is False, `not_c` is False, `i` is equal to the length of `set_`.
    #
    #Explanation: After the loop completes all its iterations, the value of `A` alternates starting from `False` (since it starts as `True` and changes each iteration). The variable `not_c` remains `False` because it is set to `False` when the condition `set_[i] - set_[i - 1] > 1` is met, which causes the loop to break. Since the loop breaks as soon as the condition is met, `not_c` does not change back to `True`. The variable `i` will be equal to the length of `set_` because the loop increments `i` from 1 up to `len(set_) - 1`, and then the loop ends.
    if not_c :
        A = not A
    #State: `A` is False, `not_c` is False, `i` is equal to the length of `set_`.
    return 'Alice' if A else 'Bob'
    #The program returns 'Bob'
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and processes it to determine whether the first unique element is 1 and checks the gaps between consecutive unique elements. If the first unique element is not 1 or if any gap between consecutive unique elements is greater than 1, the function returns 'Alice'. Otherwise, it alternates the boolean value of `A` and returns 'Bob' based on the final value of `A`.

