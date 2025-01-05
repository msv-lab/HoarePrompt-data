#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5; and a is a list of n positive integers where each a[i] (1 ≤ a[i] ≤ 10^9).
def func():
    rstr = lambda : stdin.readline().strip()
    rstrs = lambda : [str(x) for x in stdin.readline().split()]
    rstr_2d = lambda n: [rstr() for _ in range(n)]
    rint = lambda : int(stdin.readline())
    rints = lambda : [int(x) for x in stdin.readline().split()]
    rint_2d = lambda n: [rint() for _ in range(n)]
    rints_2d = lambda n: [rints() for _ in range(n)]
    pr = lambda args, sep: stdout.write(sep.join(map(str, args)) + '\n')
    ceil1, out = lambda a, b: (a + b - 1) // b, []
    for _ in range(int(input())):
        n, a = rint(), sorted(rints())
        
        be, en, ans = 0, n - 1, n
        
        while be <= en:
            md = be + en >> 1
            su = sum(a[:md + 1])
            for i in range(md + 1, n):
                if su < a[i]:
                    su = -1
                    break
                su += a[i]
            if su == -1:
                be = md + 1
            else:
                en = md - 1
                ans = md + 1
        
        out.append(n - ans + 1)
        
        out.append(' '.join(map(str, [x for x in range(ans, n + 1)])))
        
    #State of the program after the  for loop has been executed: `out` is a list containing the results of all iterations, `n` remains unchanged, `a` remains unchanged, `be` is greater than `en`, and `ans` is the largest index where the condition holds.
    pr(out, '\n')
#Overall this is what the function does:The function accepts multiple test cases, each consisting of a positive integer `n` and a list `a` of `n` positive integers. It processes these cases to determine the largest index such that the sum of the selected integers is less than or equal to the next integer in the sorted list. The function outputs the count of integers that can be included based on this condition and their respective indices in the original list. It handles up to 10,000 test cases and each list can contain up to 200,000 integers, with integers ranging from 1 to 10^9.

