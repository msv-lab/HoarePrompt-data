#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^5, and h is a list of n positive integers where each integer hi satisfies 1 ≤ hi ≤ 10^9.
def func():
    n = int(sys.stdin.next())
    floors = map(int, sys.stdin.next().split(' '))
    m = 0
    s = []
    for h in floors[::-1]:
        s.append('%i' % (m - h + 1 if m - h + 1 > 0 else 0))
        
        m = max(h, m)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 10^5; `floors` is a map object containing at least 1 integer; `m` is the maximum value found in `floors`; `s` is a list containing formatted strings based on each floor value and the maximum value `m` calculated during the iteration.
    print(' '.join(s[::-1]).strip())
#Overall this is what the function does:The function reads a positive integer `n` and a list of `n` positive integers from standard input, then calculates a new list where each element represents the difference between the maximum floor value seen so far and the current floor, adjusted to be at least zero. Finally, it prints this list in reverse order as a space-separated string. The function does not explicitly return any value.

