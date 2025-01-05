#State of the program right berfore the function call: Each query value ni is a positive integer greater than 1.**
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: The final output will depend on the input values. For odd input values, the loop will subtract 9 from the input value and set c to 1. If the input value is in (1, 2, 3, 5, 7, 11), the loop will print -1. Otherwise, it will print the input value divided by 4 plus c.
#Overall this is what the function does:The function `func` iterates over a range of values based on user input. For each iteration, it takes an input value `a`, performs certain operations based on whether `a` is odd, and then prints a specific output. If `a` is odd, it subtracts 9 from `a` and sets `c` to 1. It then checks if `a` is in a predefined set of values and prints -1 if it is, otherwise it prints the result of `a` divided by 4 plus `c`. The function does not accept any parameters and does not have a return value.

