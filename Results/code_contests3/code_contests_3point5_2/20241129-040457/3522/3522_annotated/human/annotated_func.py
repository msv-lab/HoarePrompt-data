#State of the program right berfore the function call: **
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, the final values of `a` and `c` will be determined by the input values provided during the loop execution. If `a` is odd, it will be decreased by 9 and `c` will be set to 1. If `a` is even, `c` will remain 0. Then, the final output will be -1 if `a` is in (1, 2, 3, 5, 7, 11), otherwise it will be the result of `a / 4 + c`.
#Overall this is what the function does:The function `func` does not accept any parameters. It iterates over a range of values based on user input, modifies the value `a` based on whether it is odd or even, calculates a result based on `a`, and prints the result. If `a` is odd, it decreases by 9 and sets `c` to 1. The final output is -1 if `a` is in (1, 2, 3, 5, 7, 11), otherwise it is the result of `a / 4 + c`. The function does not return any value.

