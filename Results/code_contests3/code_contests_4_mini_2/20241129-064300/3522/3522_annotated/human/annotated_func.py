#State of the program right berfore the function call: q is a positive integer such that 1 ≤ q ≤ 10^5, and each ni is a positive integer such that 1 ≤ ni ≤ 10^9.
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `q` is a positive integer such that 1 ≤ `q` ≤ 10^5; `a` is the last input integer processed; `c` is either 0 or 1 depending on whether the last `a` was odd; the output of the print statement is either -1 if the last `a` is in (1, 2, 3, 5, 7, 11) or else the value of `a / 4 + c.
#Overall this is what the function does:The function accepts a series of positive integers and for each integer, it checks if it is odd. If it is odd, it subtracts 9 from it and sets a flag `c` to 1. The function then prints -1 if the resulting integer is in the set {1, 2, 3, 5, 7, 11}; otherwise, it prints the result of integer division of the integer by 4, adjusted by `c`. The function processes multiple integers based on user input, but it does not return any values directly.

