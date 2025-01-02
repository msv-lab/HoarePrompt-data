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
        
    #State of the program after the  for loop has been executed: `i` is `n`, `cur` is the smallest integer such that `(cur - 1) * i > n`, `n` must satisfy this condition, `ans` is `2 * cur * (cur - 1)`
    print(ans)
#Overall this is what the function does:The function calculates a specific mathematical value based on the input integer `n`. It starts by reading an integer `n` from standard input, where `2 ≤ n ≤ 100 000`. For each integer `i` starting from 2 up to `n`, it finds the smallest integer `cur` such that `i * cur` exceeds `n`. It then adds `4 * cur` to the accumulator `ans`. After the loop completes, it prints the final value of `ans`. The function does not accept any parameters and returns nothing. Potential edge cases include the minimum and maximum values of `n`, and the case when `n` is exactly equal to 2, where `ans` would be 4 since the loop would not execute.

