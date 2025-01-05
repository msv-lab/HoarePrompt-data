#State of the program right berfore the function call: Each query integer ni is a positive integer greater than 1.**
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `a` and `c` are integers, output is either -1 or the result of the expression `a / 4 + c`
#Overall this is what the function does:Functionality: The function `func` iterates over a series of queries. For each query, it takes an input integer `a`, performs a calculation on `a` based on whether it is odd, and then prints either -1 or the result of the expression `a / 4 + c`. The function does not accept any parameters and does not explicitly return any value. It handles odd numbers by subtracting 9 from them and setting `c` to 1. It then checks if `a` is in a specific set of values and prints -1 if it is, or the result of `a / 4 + c` otherwise.

