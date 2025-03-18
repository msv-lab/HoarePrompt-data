#State of the program right berfore the function call: a is a list of integers where 2 <= len(a) <= 100 and 1 <= a_i <= 10^9 for all i. num2 is an integer representing the length of the list a, such that num2 == len(a).
def func_1(a, num2):
    order = 0
    for i in range(1, num2):
        if a[i - 1] >= a[i]:
            order += 1
        
    #State: `a` is a list of integers where `2 <= len(a) <= 100` and `1 <= a_i <= 10^9` for all `i`. `num2` is an integer representing the length of the list `a` such that `num2 == len(a)`. `order` is the count of times an element in `a` is greater than or equal to the next element in the list.
    if (order == 0) :
        return True
        #The program returns True
    else :
        return False
        #The program returns False
#Overall this is what the function does:The function checks if a list of integers `a` is strictly increasing. It returns `True` if every element in the list is less than the next element, and `False` otherwise.

