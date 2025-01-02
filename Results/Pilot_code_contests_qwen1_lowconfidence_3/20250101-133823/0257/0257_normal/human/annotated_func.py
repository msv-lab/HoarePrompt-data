#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 100 000.
def func():
    rstr = lambda : stdin.readline().strip()
    rstrs = lambda : [str(x) for x in stdin.readline().split()]
    rint = lambda : int(stdin.readline())
    rints = lambda : [int(x) for x in stdin.readline().split()]
    rstr_2d = lambda n: [rstr() for _ in range(n)]
    rint_2d = lambda n: [rint() for _ in range(n)]
    rints_2d = lambda n: [rints() for _ in range(n)]
    pr = lambda args, sep: stdout.write(sep.join(map(str, args)) + '\n')
    out = []
    n, ans = int(input()), 0
    for i in range(2, n + 1):
        cur = 2
        
        while i * cur <= n:
            ans += 4 * cur
            cur += 1
        
    #State of the program after the  for loop has been executed: `n` is an integer greater than or equal to 6, `ans` is the sum of `4 * cur` for each iteration where `cur` started from 2 and incremented until the condition `i * cur > n` is met for the last executed iteration, `cur` is the final value of `cur` after the loop, `i` is the final value of `i` after the loop terminates.
    print(ans)
#Overall this is what the function does:The function calculates the sum of values `4 * cur` for each iteration where `cur` starts from 2 and increments until the condition `i * cur > n` is met for the last executed iteration. Specifically, it iterates over all integers `i` from 2 to `n`, and for each `i`, it adds `4 * cur` to the variable `ans` while `i * cur` is less than or equal to `n`. The function takes no explicit parameters but reads `n` from standard input, where `2 ≤ n ≤ 100 000`. After the function concludes, the final state of the program is that `ans` contains the computed sum, and `n` retains its original value read from input. No output is explicitly returned; instead, the result `ans` is printed to standard output. Potential edge cases include the minimum value of `n` (2), where only one iteration occurs, and the maximum value of `n` (100,000), which may involve a large number of iterations. The function does not handle invalid inputs for `n` other than checking the bounds, and it assumes valid integer input within the specified range.

