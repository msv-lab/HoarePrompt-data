#State of the program right berfore the function call: **
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `a` is the input value after all modifications, `c` is 1 if the last `a` value was odd, otherwise `c` remains 0
#Overall this is what the function does:The function does not accept any parameters. It iterates over a range of values provided by the user and modifies each input value `a` based on whether it is odd or even. If `a` is odd, it subtracts 9 from `a` and sets `c` to 1. Then, it checks if the modified `a` is in a specific set of numbers and prints -1 if it is, otherwise it calculates `a` divided by 4 and adds `c` to the result. The function does not have a specific return value.

