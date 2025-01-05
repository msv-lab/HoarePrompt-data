#State of the program right berfore the function call: **Precondition**: **a and b are integers such that 1 <= a,b <= 10^9 and a <= b.**
def func_1(a, b):
    if (a > b) :
        return a - b
        #The program returns the result of subtracting 'b' from 'a', where 'a' and 'b' are integers such that 1 <= a,b <= 10^9 and a > b.
    #State of the program after the if block has been executed: *a and b are integers such that 1 <= a,b <= 10^9 and a <= b. The condition (a > b) is false, which means a is less than or equal to b
    return b - a
    #The program returns the result of subtracting 'a' from 'b', where 'a' and 'b' are integers such that 1 <= a,b <= 10^9 and a <= b. The condition (a > b) is false, which means a is less than or equal to b
#Overall this is what the function does:The function func_1 accepts two integer parameters a and b, where a and b are within the range 1 to 10^9 and a is less than or equal to b. If a is greater than b, the function returns the result of subtracting b from a. If a is less than or equal to b, the function returns the result of subtracting a from b.

