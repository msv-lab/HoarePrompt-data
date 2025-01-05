#State of the program right berfore the function call: **
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`c` is the sum of variables `a` and `b`. If `c` is greater than or equal to `mod`, then `c` is updated to a new value after subtracting `mod`. Otherwise, there is no change in the value of `c`.
    return c
    #The program returns the sum of variables `a` and `b` after checking if it is greater than or equal to `mod`, and updating `c` accordingly by subtracting `mod` if necessary.
#Overall this is what the function does:The function func_1 accepts two integer parameters a and b, calculates their sum, and returns the result. If the sum of a and b is greater than or equal to the variable mod, the function subtracts mod from the sum before returning it. However, the actual code does not handle cases where `mod` is not defined or initialized. Therefore, if `mod` is not provided or initialized, the function might encounter an error.

#State of the program right berfore the function call: N and K are non-negative integers such that 1 <= N <= 2 * 10^5 and 0 <= K <= 2 * 10^5. H_i is an integer such that 1 <= H_i <= 10^9 for each i.**
def func_2():
    H, N = [int(x) for x in raw_input().split()]
    s = sum([int(x) for x in raw_input().split()])
    if (s >= H) :
        print('Yes')
    else :
        print('No')
    #State of the program after the if-else block has been executed: *`N` and `K` are non-negative integers such that 1 <= N <= 2 * 10^5 and 0 <= K <= 2 * 10^5. `H_i` is an integer such that 1 <= H_i <= 10^9 for each i; `H` and `N` are assigned input integers, `s` is the sum of integers entered through input split by spaces. If the sum `s` is greater than or equal to `H`, the program executes the if part. If the sum of integers entered through input split by spaces is less than `H`, the program executes the else part.
#Overall this is what the function does:The function func_2 reads two integers H and N from user input, calculates the sum of N integers entered through input, and then prints 'Yes' if the sum is greater than or equal to H, otherwise it prints 'No'. The program does not accept any parameters and performs these operations internally based on user input.

