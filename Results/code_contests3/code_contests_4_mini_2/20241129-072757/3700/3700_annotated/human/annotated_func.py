#State of the program right berfore the function call: a is a non-negative integer representing the number of monsters (N) such that 1 <= a <= 200000, b is a non-negative integer representing the maximum number of Special Moves (K) such that 0 <= b <= 200000, and the remaining input consists of a list of integers representing the health of each monster (H) where each health value is in the range 1 <= H_i <= 10^9.
def func_1(a, b):
    c = a + b
    if (c >= mod) :
        c -= mod
    #State of the program after the if block has been executed: *`a` is a non-negative integer between 1 and 200000, `b` is a non-negative integer between 0 and 200000, and `c` is a non-negative integer representing the sum of `a` and `b`. If `c` is greater than or equal to `mod`, then `c` is updated to be `c - mod`. If `c` is less than `mod`, no changes are made to `c`.
    return c
    #The program returns the value of c, which is the sum of a and b, adjusted if it is greater than or equal to mod.
#Overall this is what the function does:The function accepts two non-negative integers `a` and `b`, representing the number of monsters and the maximum number of Special Moves, respectively. It calculates their sum `c`. If `c` is greater than or equal to a predefined constant `mod`, it subtracts `mod` from `c`. The function then returns the adjusted value of `c`, which is the sum of `a` and `b`, potentially reduced by `mod` if the sum exceeds `mod`.

#State of the program right berfore the function call: N is an integer such that 1 <= N <= 200000; K is a non-negative integer such that 0 <= K <= 200000; H is a list of integers where each H_i (1 <= i <= N) satisfies 1 <= H_i <= 10^9.
def func_2():
    H, N = [int(x) for x in raw_input().split()]
    s = sum([int(x) for x in raw_input().split()])
    if (s >= H) :
        print('Yes')
    else :
        print('No')
    #State of the program after the if-else block has been executed: *`N` is the first integer from input; `H` is a list of integers from the remaining input; `s` is the sum of all integers from the new input. If `s` is greater than or equal to the sum of the elements in list `H`, 'Yes' is printed. Otherwise, if `s` is less than the sum of the elements in list `H`, 'No' is printed.
#Overall this is what the function does:The function accepts an integer `N` and reads a list of integers from input. It computes the sum of another list of integers and checks if this sum is greater than or equal to the integer `H`, printing 'Yes' if it is, and 'No' otherwise. The function does not utilize `K` and interprets `H` as a single integer, not a list.

