#State of the program right berfore the function call: Each query contains a single positive integer ni (1 ≤ ni ≤ 10^9).**
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `ni` is 1, `a` is updated based on the conditions within the loop, `c` is either 0 or 1, the result is either -1 or the division of `a` by 4 added with `c`.
#Overall this is what the function does:The function `func` reads a series of positive integers `a` from the user, adjusts the value of `a` based on whether it is odd, and then calculates a result based on specific conditions. If `a` is odd, it subtracts 9 from `a` and sets `c` to 1. It then checks if `a` is in a predefined set of numbers, and if it is, it prints -1; otherwise, it calculates `a` divided by 4 and adds `c` to the result. The function does not accept any parameters and does not have a specific return value.

