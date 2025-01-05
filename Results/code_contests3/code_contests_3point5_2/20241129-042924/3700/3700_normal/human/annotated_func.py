#State of the program right berfore the function call: **
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`a`, `b`, `c` are integers. If `c` is greater than or equal to `mod`, then `c` is less than `mod`.
    return c
    #The program returns the integer 'c', where 'c' is guaranteed to be less than 'mod' if 'c' is greater than or equal to 'mod'
#Overall this is what the function does:The function `func_1` accepts two integer parameters `a` and `b`, calculates their sum, and assigns it to variable `c`. If the sum of `a` and `b` is greater than or equal to the value of `mod`, `c` is adjusted to be less than `mod`. The function then returns the final value of `c`. The functionality of the function is to ensure that the returned value `c` is always less than `mod` if it was originally greater than or equal to `mod`.

#State of the program right berfore the function call: N and K are non-negative integers, 1 <= H_i <= 10^9 for all i.**
def func_2():
    H, N = [int(x) for x in raw_input().split()]
    s = sum([int(x) for x in raw_input().split()])
    if (s >= H) :
        print('Yes')
    else :
        print('No')
    #State of the program after the if-else block has been executed: *N and K are non-negative integers, 1 <= H_i <= 10^9 for all i, H and N are assigned values based on the input split operation, s contains the sum of the input integers. If the sum of the input integers is greater than or equal to H, the program executes the if part. Otherwise, the program executes the else part and prints 'No'.
#Overall this is what the function does:The function `func_2` does not accept any parameters. It reads two integers H and N from the input, calculates the sum of N integers also from the input, and then prints 'Yes' if the sum is greater than or equal to H, otherwise it prints 'No'. Therefore, the functionality of the function is to compare the sum of N integers with a given value H and output 'Yes' or 'No' based on the comparison.

