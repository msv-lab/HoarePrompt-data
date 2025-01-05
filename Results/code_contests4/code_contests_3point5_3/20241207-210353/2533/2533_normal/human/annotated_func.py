#State of the program right berfore the function call: n is a positive integer, x1, y1, x2, y2 are integers such that 0 <= x1 <= x2 <= 100000 and 0 <= y1 <= y2 <= 100000. rix, riy, vix, viy are integers such that 0 <= rix, riy <= 100000 and -100000 <= vix, viy <= 100000.**
def func_1():
    for line in sys.stdin:
        for value in line.split():
            yield value
        
    #State of the program after the  for loop has been executed: Output State: n is a positive integer, all the values from sys.stdin have been processed and yielded for each iteration of the loop.
#Overall this is what the function does:The function `func_1` reads input from `sys.stdin` line by line and yields each value from the input. It does not accept any parameters. The function does not have a specific return value defined.

