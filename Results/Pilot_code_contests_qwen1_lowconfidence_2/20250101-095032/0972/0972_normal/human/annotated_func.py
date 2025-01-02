#State of the program right berfore the function call: The input consists of two integers n and m, where 2 ≤ n ≤ 100 000 and 1 ≤ m ≤ 10 000, and n ≥ 2m. The next n lines contain the surnames (strings of length from 1 to 10 characters and consisting of large and small English letters), region numbers (integers from 1 to m), and the number of points scored by the participants (integers from 0 to 800, inclusive). All surnames are distinct, and at least two people participated from each of the m regions. Surnames that only differ in letter cases are considered distinct.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    rstrs = lambda : [str(x) for x in stdin.readline().split()]
    n, m = rints()
    mem, ans = [[] for _ in range(m + 1)], []
    for _ in range(n):
        a = rstrs()
        
        mem[int(a[1])].append((int(a[-1]), a[0]))
        
    #State of the program after the  for loop has been executed: `n` is the first integer read from the input and satisfies \(2 \leq n \leq 100,000\) and \(n \geq 2m\); `m` is the second integer read from the input and satisfies \(1 \leq m \leq 10,000\); `mem` is a list of \(m + 1\) sublists, each containing zero or more tuples of the form \((\text{integer}, \text{string})\), where each tuple corresponds to a value returned by the function `rstrs()` and the index of the sublist to which the tuple is appended is determined by the value of `int(a[1])` in the call to `rstrs()`; `ans` is an empty list; `_` is \(n\).
    for i in range(1, m + 1):
        mem[i].sort()
        
        tem = mem[i]
        
        if len(tem) > 2 and tem[-3][0] in (tem[-1][0], tem[-2][0]):
            ans.append('?')
        else:
            ans.append('%s %s' % (tem[-1][1], tem[-2][1]))
        
    #State of the program after the  for loop has been executed: `i` is `m + 1`, `m` is a valid integer within the range \(1 \leq m \leq 10,000\), `mem` is a list of \(m + 1\) sublists, each sublist is sorted, `ans` is a list of length `m + 1`, where each element is either `'?'` or a string in the format `'%s %s' % (tem[-1][1], tem[-2][1])`, depending on the conditions specified in the loop.
    print('\n'.join(ans))
#Overall this is what the function does:The function processes input data consisting of surnames, region numbers, and scores for participants. It organizes this data into a list of lists, where each sublist contains tuples of scores and surnames associated with a specific region. After sorting each sublist based on scores, the function checks if the third-highest score in any region is equal to the highest or second-highest score. If this condition is met, it appends '?' to the result list; otherwise, it appends the surnames of the highest and second-highest scoring participants. The function then prints the result list, which contains either '?' or formatted strings representing the surnames of the top two scorers in each region. The function handles the case where there are fewer than three participants in a region by defaulting to printing the top two available.

