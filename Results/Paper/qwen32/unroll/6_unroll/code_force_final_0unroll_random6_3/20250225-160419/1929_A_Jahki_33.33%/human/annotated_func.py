#State of the program right berfore the function call: a is a list of integers where 2 <= len(a) <= 100 and 1 <= a_i <= 10^9 for each element a_i in a. num2 is an integer representing the length of the array a, so num2 should be equal to len(a).
def func_1(a, num2):
    order = 0
    for i in range(1, num2):
        if a[i - 1] >= a[i]:
            order += 1
        
    #State: `a` is a list of integers where 2 <= len(a) <= 100 and 1 <= a_i <= 10^9 for each element a_i in a; `num2` is equal to len(a); `order` is the number of non-increasing consecutive pairs in the list a.
    if (order == 0) :
        return True
        #The program returns True
    else :
        return False
        #The program returns False
#Overall this is what the function does:The function `func_1` checks if the list `a` of integers is strictly increasing. It returns `True` if the list is strictly increasing, meaning each element is greater than the previous one, and `False` otherwise.

