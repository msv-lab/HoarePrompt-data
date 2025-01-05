#State of the program right berfore the function call: a is a non-negative integer representing the number of monsters (N) such that 1 <= a <= 200000, b is a non-negative integer representing the maximum number of Special Moves (K) such that 0 <= b <= 200000, and the subsequent input must be a list of integers representing the health of each monster (H_i) where each H_i is an integer such that 1 <= H_i <= 10^9.
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`a`, `b`, and `c` are non-negative integers. If `c` is greater than or equal to `mod`, then `c` is decremented by `mod`. If `c` is less than `mod`, the values of `a`, `b`, and `c` remain unchanged.
    return c
    #The program returns the value of `c`, which is either unchanged if it was less than `mod`, or decremented by `mod` if it was greater than or equal to `mod`.
#Overall this is what the function does:The function accepts two non-negative integers `a` and `b`, computes their sum `c`, and returns `c` decremented by `mod` if `c` is greater than or equal to `mod`. If `c` is less than `mod`, it returns `c` unchanged. The function does not handle any edge cases related to the parameters being out of bounds since it assumes valid input within the specified ranges.

#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 200000, K is a non-negative integer such that 0 <= K <= 200000, and H is a list of N positive integers where each H[i] (1 <= i <= N) is such that 1 <= H[i] <= 10^9.
def func_2():
    H, N = [int(x) for x in raw_input().split()]
    s = sum([int(x) for x in raw_input().split()])
    if (s >= H) :
        print('Yes')
    else :
        print('No')
    #State of the program after the if-else block has been executed: *`H` is a list of integers derived from the input, `N` is the number of elements in `H`, and `s` is the sum of the integers from user input. If `s` is greater than or equal to the list `H`, 'Yes' is printed. If `s` is less than the minimum value of `H` (if `H` is not empty) or if `H` is an empty list, 'No' is printed.
#Overall this is what the function does:The function reads an integer `H` and a list of integers, sums the list, and prints 'Yes' if the sum is greater than or equal to `H`, and 'No' otherwise. It does not handle cases of empty input or incorrect input types.

