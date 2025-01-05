#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 10^5, and h is a list of n positive integers where each integer hi satisfies 1 ≤ hi ≤ 10^9.
def func():
    n = int(sys.stdin.next())
    floors = map(int, sys.stdin.next().split(' '))
    m = 0
    s = []
    for h in floors[::-1]:
        s.append('%i' % (m - h + 1 if m - h + 1 > 0 else 0))
        
        m = max(h, m)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that 1 ≤ `n` ≤ 10^5; `m` is the maximum height from `floors`; `s` is a list containing `n` integers representing the results of the calculations performed during the iterations.
    print(' '.join(s[::-1]).strip())
#Overall this is what the function does:The function accepts a positive integer `n`, which indicates the number of heights in a list `h`, and processes this list to calculate a new list `s`. The list `s` contains the difference between the current maximum height observed and each height in the list, adjusted to ensure that negative values are replaced with zero. Finally, the function prints the values in `s` in the original order. The function does not return anything but outputs the result directly.

