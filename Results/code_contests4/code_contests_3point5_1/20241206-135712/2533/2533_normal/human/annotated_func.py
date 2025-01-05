#State of the program right berfore the function call: **Precondition**: 
- n is a positive integer such that 1 ≤ n ≤ 100,000.
- x1, y1, x2, y2 are non-negative integers such that 0 ≤ x1 ≤ x2 ≤ 100,000 and 0 ≤ y1 ≤ y2 ≤ 100,000.
- rix, riy, vix, viy are integers such that 0 ≤ rix, riy ≤ 100,000 and -100,000 ≤ vix, viy ≤ 100,000.
def func_1():
    for line in sys.stdin:
        for value in line.split():
            yield value
        
    #State of the program after the  for loop has been executed: The loop will continue to execute as long as there is input available from `sys.stdin` to be split and yielded one by one. The loop will stop when there is no more input available. `line` will be a string with multiple values when split, and `value` will yield each value after splitting `line`.
#Overall this is what the function does:The function func_1 reads input from sys.stdin, splits the input lines into values, and yields each value. This process continues until there is no more input available. The function does not accept any parameters and does not explicitly return any values. It acts as a generator for processing input values from sys.stdin.

