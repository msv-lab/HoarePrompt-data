#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5; a is a list of n positive integers where each integer a_i satisfies 1 ≤ a_i ≤ 10^9. The sum of n over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `out` contains the results of the calculations performed in all iterations of the outer loop, `_` is equal to the number of iterations executed, `n` is a non-negative integer greater than or equal to 3, `be` is greater than `en`, `md` is the last calculated mid-point index, `ans` is the maximum valid index found across all iterations, and `su` represents the last calculated sum value based on the evaluations performed in the inner loop.
    pr(out, '\n')
#Overall this is what the function does:The function accepts multiple test cases, where each test case consists of a positive integer `n` and a list `a` of `n` positive integers. It processes each test case to determine the maximum number of elements from the list that can be summed without exceeding the next largest element and returns the count of such elements. Additionally, it outputs the indices of these elements in the sorted list. The function handles cases where no elements can be summed without exceeding the next element and returns appropriate results based on the input constraints.

