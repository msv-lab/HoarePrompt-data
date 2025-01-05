#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100000; (x1, y1) and (x2, y2) are integers representing the coordinates of opposite corners of the mousetrap with 0 <= x1 <= x2 <= 100000 and 0 <= y1 <= y2 <= 100000; each mouse's initial position (rix, riy) and speed (vix, viy) are integers such that 0 <= rix, riy <= 100000 and -100000 <= vix, viy <= 100000.
def func_1():
    for line in sys.stdin:
        for value in line.split():
            yield value
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 <= `n` <= 100000; `line` is a non-empty string from sys.stdin; `value` is the last word from the last non-empty line processed, and all words from each line in sys.stdin have been yielded.
#Overall this is what the function does:The function processes input from standard input (stdin) line by line, yielding each word encountered in the lines. It does not return any defined value, but instead, it generates a sequence of words from the input, which can be utilized for further processing. The function does not handle any specific parameters related to mice or a mousetrap, and no actual calculations or logic regarding mice's positions or speeds are implemented.

