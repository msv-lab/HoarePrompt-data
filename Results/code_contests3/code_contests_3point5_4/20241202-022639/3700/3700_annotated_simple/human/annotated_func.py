#State of the program right berfore the function call: **
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`a`, `b`, `c` are integers. If `c` is the result of `a + b` and `c` is greater than or equal to `mod`, then `c` is updated to the result of `a + b` minus `mod`, and the new value of `c` is less than `mod`. Otherwise, there is no change in the values of `a`, `b`, and `c`.
    return c
    #The program returns the updated value of 'c' which is less than 'mod' after the specified condition is applied
#Overall this is what the function does:The function `func_1` accepts two parameters `a` and `b`, calculates their sum, and if the sum is greater than or equal to `mod`, it subtracts `mod` from the sum and returns the updated value. The function ensures that the returned value of `c` is always less than `mod`. If the sum of `a` and `b` is less than `mod`, the function returns the sum without any modifications.

#State of the program right berfore the function call: N and K are non-negative integers such that 1 <= N <= 2 * 10^5 and 0 <= K <= 2 * 10^5. H_i is a positive integer such that 1 <= H_i <= 10^9 for each i from 1 to N.**
def func_2():
    H, N = [int(x) for x in raw_input().split()]
    s = sum([int(x) for x in raw_input().split()])
    if (s >= H) :
        print('Yes')
    else :
        print('No')
    #State of the program after the if-else block has been executed: *H is a list of positive integers ranging from 1 to 10^9, N is a non-negative integer ranging from 1 to 2 * 10^5, s is the sum of the entered integers. If the sum of the entered integers is greater than or equal to the elements in list H, then the overall sum s is equal to H. Otherwise, the sum s is less than H.
#Overall this is what the function does:The function `func_2` reads two inputs: a list of integers `H` and an integer `N`. It then calculates the sum `s` of another list of integers. If the sum `s` is greater than or equal to the elements in list `H`, it prints 'Yes'; otherwise, it prints 'No'. The function does not accept any parameters and operates based on the constraints provided for `N`, `K`, and `H_i`.

