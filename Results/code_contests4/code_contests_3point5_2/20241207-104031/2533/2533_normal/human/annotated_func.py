#State of the program right berfore the function call: n is a positive integer, x1, y1, x2, y2 are non-negative integers such that 0 <= x1 <= x2 <= 100000 and 0 <= y1 <= y2 <= 100000. rix, riy, vix, viy are integers such that 0 <= rix, riy <= 100000 and -100000 <= vix, viy <= 100000.**
def func_1():
    for line in sys.stdin:
        for value in line.split():
            yield value
        
    #State of the program after the  for loop has been executed: n is a positive integer, x1, y1, x2, y2 are non-negative integers such that 0 <= x1 <= x2 <= 100000 and 0 <= y1 <= y2 <= 100000, rix, riy, vix, viy are integers such that 0 <= rix, riy <= 100000 and -100000 <= vix, viy <= 100000. The loop will execute as long as there are values being input from sys.stdin, and the generator function yields all values input from sys.stdin.
#Overall this is what the function does:The function `func_1` reads values from the standard input using a generator function within a nested loop. It does not accept any parameters and continues to read values until there are no more inputs from the standard input. The function does not provide any specific output based on the information given.

