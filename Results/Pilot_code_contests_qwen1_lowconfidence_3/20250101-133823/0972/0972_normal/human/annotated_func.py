#State of the program right berfore the function call: There are two lists provided: one list `n` containing the number of participants (an integer) and the number of regions (an integer), and another list of strings describing the participants in the qualifying competition format (surname, region number, and points scored). The surnames are unique, and each region has at least two participants.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    rstrs = lambda : [str(x) for x in stdin.readline().split()]
    n, m = rints()
    mem, ans = [[] for _ in range(m + 1)], []
    for _ in range(n):
        a = rstrs()
        
        mem[int(a[1])].append((int(a[-1]), a[0]))
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `m` is an integer read from standard input, the list of strings describing the participants is unchanged, `mem` is a list of `m + 1` lists where each list contains tuples of the form `(int(a[-1]), a[0])` with `a[1]` being the index, `ans` is an empty list, `a` is the result of `rstrs()` if the loop executed at least once. If the loop did not execute, `n` must be 0, `mem` remains unchanged, and `ans` remains an empty list.
    for i in range(1, m + 1):
        mem[i].sort()
        
        tem = mem[i]
        
        if len(tem) > 2 and tem[-3][0] in (tem[-1][0], tem[-2][0]):
            ans.append('?')
        else:
            ans.append('%s %s' % (tem[-1][1], tem[-2][1]))
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `m` is a positive integer, `i` is `m`, the list of strings describing the participants is unchanged, `mem` is a list of `m + 1` lists where each list contains tuples of the form `(int(a[-1]), a[0])` with `a[1]` being the index, `ans` is a list containing a series of strings based on the conditions inside the loop. If the loop does not execute, `n` must be 0, `mem` remains unchanged, and `ans` remains an empty list. If the loop executes, `ans` contains a series of strings where each string is either `'second_last_element_of_mem[i][1] last_element_of_mem[i][1]'` or `'?'` depending on whether the condition `len(mem[i]) > 2 and mem[i][-3][0] in (mem[i][-1][0], mem[i][-2][0])` holds true for each iteration.
    print('\n'.join(ans))
#Overall this is what the function does:The function accepts a list `n` containing two integers representing the number of participants and the number of regions, and a list of strings describing participants in the format (surname, region number, and points scored). It processes the participant data to determine the second and first-place winners for each region. If a region has more than three participants and the third-place score is the same as the first or second place, it marks the region as uncertain ('?'). Otherwise, it appends the names of the first and second-place winners. The function then prints a list of these results for each region, separated by newlines.

