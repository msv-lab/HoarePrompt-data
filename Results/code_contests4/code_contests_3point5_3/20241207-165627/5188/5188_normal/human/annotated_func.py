#State of the program right berfore the function call: **Precondition**: **a and b are integers such that 1 ≤ a, b ≤ 10^9.**
def func_1(a, b):
    if (a > b) :
        return a - b
        #The program returns the result of subtracting integer b from integer a, where a and b are integers such that 1 ≤ a, b ≤ 10^9 and a is greater than b
    #State of the program after the if block has been executed: *a and b are integers such that 1 ≤ a, b ≤ 10^9. a is less than or equal to b
    return b - a
    #The program returns the result of subtracting 'a' from 'b', where 'a' and 'b' are integers such that 1 ≤ a, b ≤ 10^9 and a is less than or equal to b
#Overall this is what the function does:Functionality: The function `func_1` accepts two integer parameters `a` and `b`, both within the range 1 ≤ a, b ≤ 10^9. If `a` is greater than `b`, the function returns the result of subtracting `b` from `a`. If `a` is less than or equal to `b`, the function returns the result of subtracting `a` from `b`. However, one potential edge case that is missing from the annotations is when `a` is equal to `b`, in which case the function would return 0.

