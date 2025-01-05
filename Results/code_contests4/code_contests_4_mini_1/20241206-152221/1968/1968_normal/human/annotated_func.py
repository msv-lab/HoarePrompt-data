#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, followed by a list of n positive integers a_i where 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `out` is a list containing the results of each iteration, including the values `n - ans + 1` and strings of integers from `ans` to `n` for each input case, `be` is greater than `en`, `ans` is the maximum valid size of the subset found across all iterations, and `su` is the last calculated sum of elements from `a[0]` to `a[md]` or -1 if the condition was met during the last iteration.
    pr(out, '\n')
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a positive integer `n` and a list of `n` positive integers `a_i`. It determines the maximum size of a subset of `a` such that the sum of the subset is greater than or equal to each of its elements. The function returns the number of elements that cannot be included in such a subset and the corresponding elements of the list that make up that subset. If no valid subset is found, it may return `n` as the size of the excluded elements.

