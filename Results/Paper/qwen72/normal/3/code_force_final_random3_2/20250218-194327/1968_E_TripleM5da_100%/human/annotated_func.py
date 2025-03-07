#State of the program right berfore the function call: t is an integer such that 1 <= t <= 50, and n is an integer for each test case such that 2 <= n <= 10^3.
def func():
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: `t` is an integer such that 1 <= t <= 50, `n` must be a positive integer, and all iterations of the loop have been completed.
#Overall this is what the function does:The function `func` reads an integer `t` (1 <= t <= 50) from the input, indicating the number of test cases. For each test case, it reads another integer `n` (2 <= n <= 10^3) and prints a series of pairs of integers. The first two pairs are always (1, 1) and (1, 2). For each integer `i` from 3 to `n` (inclusive), it prints the pair (i, i). After all test cases are processed, the function completes and the program returns to its initial state, with no return value.

