#State of the program right berfore the function call: **
def func():
    n = int(sys.stdin.next())
    floors = map(int, sys.stdin.next().split(' '))
    m = 0
    s = []
    for h in floors[::-1]:
        s.append('%i' % (m - h + 1 if m - h + 1 > 0 else 0))
        
        m = max(h, m)
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `m` is the maximum value between all elements in `floors`, `s` is a list containing the calculated values based on the formula for each element in `floors` in reverse order
    print(' '.join(s[::-1]).strip())
#Overall this is what the function does:The function reads an integer input `n` from the standard input, then reads a list of integers `floors`, calculates specific values based on the elements in `floors` in reverse order, and prints the result. The calculated values are based on a formula that depends on the maximum value encountered in `floors`. The function does not accept any parameters and does not have a return value.

