#State of the program right berfore the function call: a is an integer representing the number of monsters (N) such that 1 <= a <= 200000, b is an integer representing the maximum number of Special Moves (K) such that 0 <= b <= 200000, and a list of integers representing the health of each monster (H_i) where 1 <= H_i <= 10^9.
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`a` is an integer representing the number of monsters (N) such that 1 <= a <= 200000; `b` is an integer representing the maximum number of Special Moves (K) such that 0 <= b <= 200000; `c` is assigned the value of `a + b`. If `c` is greater than or equal to `mod`, then `c` is updated to `a + b - mod`, ensuring that `c` remains non-negative.
    return c
    #The program returns the value of c, which is the sum of a and b, adjusted by mod if necessary to ensure it remains non-negative.
#Overall this is what the function does:The function accepts two integers, `a` (the number of monsters) and `b` (the maximum number of Special Moves), and returns the sum of `a` and `b`. If the sum is greater than or equal to a predefined constant `mod`, it subtracts `mod` from the sum to ensure the result is non-negative. There is no handling for the potential case where `mod` is not defined or has not been initialized.

#State of the program right berfore the function call: N is an integer such that 1 <= N <= 200000, K is a non-negative integer such that 0 <= K <= 200000, and H is a list of N integers where each H_i satisfies 1 <= H_i <= 10^9.
def func_2():
    H, N = [int(x) for x in raw_input().split()]
    s = sum([int(x) for x in raw_input().split()])
    if (s >= H) :
        print('Yes')
    else :
        print('No')
    #State of the program after the if-else block has been executed: *`H` is a list of integers, `N` is the integer representing the length of `H`, and `s` is the sum of integers obtained from a new input. If `s` is greater than or equal to the total of integers in list `H`, 'Yes' is printed. Otherwise, if `s` is less than the total of the integers in list `H`, 'No' is printed, and no changes are made to the values of `H`, `N`, or `s`.
#Overall this is what the function does:The function reads an integer `H` and a list of `N` integers from input, calculates the sum of a new list of integers, and prints 'Yes' if this sum is greater than or equal to `H`, or 'No' if it is less. The function does not return any value and relies on external variables for its inputs.

