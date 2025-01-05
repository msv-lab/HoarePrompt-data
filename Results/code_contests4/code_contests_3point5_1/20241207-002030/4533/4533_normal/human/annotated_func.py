#State of the program right berfore the function call: **
def func():
    n = int(sys.stdin.next())
    floors = map(int, sys.stdin.next().split(' '))
    m = 0
    s = []
    for h in floors[::-1]:
        s.append('%i' % (m - h + 1 if m - h + 1 > 0 else 0))
        
        m = max(h, m)
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `floors` is a list of integers obtained from the input, `m` is the maximum value in the `floors` list, `s` contains the calculated values based on the formula provided in the loop code for each element in `floors`.
    print(' '.join(s[::-1]).strip())
#Overall this is what the function does:The function `func` reads an integer `n` from the input, reads a list of integers `floors`, calculates a set of values based on a formula, and prints the results. It does not accept any parameters and does not return any value. The functionality includes processing the input data, calculating values based on the provided formula, and displaying the results.

