#State of the program right berfore the function call: n and m are integers such that 2 ≤ n ≤ 100 000, 1 ≤ m ≤ 10 000, and n ≥ 2m. The input consists of n lines, each describing a participant with a surname (a string of length from 1 to 10 characters and consisting of large and small English letters), a region number (an integer from 1 to m), and the number of points scored by the participant (an integer from 0 to 800, inclusive). Each region has at least two participants.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    rstrs = lambda : [str(x) for x in stdin.readline().split()]
    n, m = rints()
    mem, ans = [[] for _ in range(m + 1)], []
    for _ in range(n):
        a = rstrs()
        
        mem[int(a[1])].append((int(a[-1]), a[0]))
        
    #State of the program after the  for loop has been executed: `n` is between 2 and 100,000 inclusive, `m` is between 1 and 10,000 inclusive, `mem` is a list of `m + 1` empty lists where each sublist contains one or more tuples of the form `(int(a[-1]), a[0])`, `ans` is an empty list, `i` is `n`, `a` is the value returned by `rstrs()`
    for i in range(1, m + 1):
        mem[i].sort()
        
        tem = mem[i]
        
        if len(tem) > 2 and tem[-3][0] in (tem[-1][0], tem[-2][0]):
            ans.append('?')
        else:
            ans.append('%s %s' % (tem[-1][1], tem[-2][1]))
        
    #State of the program after the  for loop has been executed: `n` is between 2 and 100,000 inclusive, `m` is a positive integer, `mem` is a list of `m + 1` empty lists where each sublist contains one or more tuples of the form `(int(a[-1]), a[0])`, `ans` is a list containing strings either `'?'` or of the form `' %s %s' % (last_value, second_last_value)`, `i` is `m + 1`, `a` is the value returned by `rstrs()`, `tem` is `mem[m]` and is sorted. For every iteration, if `len(tem) > 2` and the third last tuple's first element is the same as either the last or second last tuple's first element, `ans` contains `'?'` appended. Otherwise, `ans` contains the string `' %s %s' % (last_value, second_last_value)` where `last_value` is the second element of the last tuple and `second_last_value` is the second element of the second-to-last tuple in `tem`.
    print('\n'.join(ans))
#Overall this is what the function does:The function reads input data describing participants, processes this data by sorting the participants within each region, and then determines and prints the top two scorers for each region. If the third highest scorer in a region has the same score as the highest or second-highest scorer, it appends '?' to the output; otherwise, it appends the names of the top two scorers. The function returns nothing but prints the results. Potential edge cases include regions with fewer than three participants, where the function will still process the available data.

