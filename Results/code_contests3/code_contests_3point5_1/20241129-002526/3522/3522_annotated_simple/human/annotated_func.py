#State of the program right berfore the function call: **
def func():
    for _ in xrange(input()):
        a = input()
        
        c = 0
        
        if a % 2 != 0:
            a = a - 9
            c = 1
        
        print - 1 if a in (1, 2, 3, 5, 7, 11) else a / 4 + c
        
    #State of the program after the  for loop has been executed: After all the iterations of the loop have finished, the final value of `a` and `c` will depend on the input values and the conditions met during the loop execution. The final printed output will either be -1 or the result of `a / 4 + c` based on the final values of `a` and `c` after the loop has completed.
#Overall this is what the function does:The function `func` does not accept any parameters. It iterates through a loop based on the user's input, updates the value of `a` and `c` based on certain conditions, and prints either -1 or the result of `a / 4 + c`. The final output is the result of the last iteration of the loop.

