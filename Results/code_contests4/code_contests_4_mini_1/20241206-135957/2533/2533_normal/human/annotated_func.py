#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 100000; (x1, y1) and (x2, y2) are integers such that 0 ≤ x1 ≤ x2 ≤ 100000 and 0 ≤ y1 ≤ y2 ≤ 100000; each mouse's initial position (rix, riy) and speed (vix, viy) are integers such that 0 ≤ rix, riy ≤ 100000 and -100000 ≤ vix, viy ≤ 100000.
def func_1():
    for line in sys.stdin:
        for value in line.split():
            yield value
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 100000; `value` is the last element yielded from the last line of input processed; if no lines were processed, `value` is undefined.
#Overall this is what the function does:The function reads lines of input from the standard input, splits each line into values, and yields each value one by one. It does not accept any parameters and does not return a final result; instead, it provides a generator that can be used to iterate through the yielded values. If no lines are processed, the last yielded value would be undefined.

