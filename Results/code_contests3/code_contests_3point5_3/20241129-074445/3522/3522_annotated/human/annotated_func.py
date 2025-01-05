#State of the program right berfore the function call: **
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: `c` is 0 or 1, `a` is an integer. If `a` is not divisible by 2, `c` is set to 1 and `a` is decreased by 9. Otherwise, `c` remains 0. The printed value is either -1 or the result of `a / 4 + c`
#Overall this is what the function does:The function does not accept any parameters. It iterates over a range of values based on user input, modifies the input value `a` by subtracting 9 if it is odd, calculates a result based on certain conditions, and prints either -1 or the result of `a / 4 + c`.

