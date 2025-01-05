#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4). For each test case, n is a positive integer (1 ≤ n ≤ 2 ⋅ 10^5) and a_i is a positive integer (1 ≤ a_i ≤ 10^9) for 1 ≤ i ≤ n.**
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
        
    #State of the program after the  for loop has been executed: At the end of the loop, the variables `be`, `en`, `ans`, `md`, `su`, `n`, `i`, `a` will have final integer values based on the conditions met during the loop execution. The list `out` will contain the final values appended throughout the loop iterations.
    pr(out, '\n')
#Overall this is what the function does:The function does not accept any parameters. It processes multiple test cases, each consisting of an integer n followed by n positive integers a_i. For each test case, it performs a binary search algorithm to find a specific value based on the input array and returns the desired output for each test case. The function utilizes lambda functions for input/output operations and binary search logic to determine the final output per test case.

