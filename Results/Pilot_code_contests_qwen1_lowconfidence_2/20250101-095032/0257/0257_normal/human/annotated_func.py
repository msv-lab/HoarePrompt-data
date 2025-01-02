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
        
    #State of the program after the  for loop has been executed: `i` is `n + 1`, `cur` is `n // (n - 1) + 1`, `ans` is the sum of `4 * cur` for all valid `i` where `2 ≤ i ≤ n`, `n` must be at least 2.
    print(ans)
#Overall this is what the function does:The function calculates a specific sum based on the input integer \( n \). It does not accept any parameters and returns no explicit value; however, the result of the calculation is printed to the standard output. The function iterates from 2 to \( n \), and for each \( i \) in this range, it increments a counter `cur` and adds \( 4 \times cur \) to the variable `ans` until \( i \times cur \) exceeds \( n \). After completing the iteration, it prints the accumulated value of `ans`. This value depends on the initial \( n \) provided, and it sums up values of \( 4 \times cur \) for all valid \( i \) where \( 2 \leq i \leq n \). The function handles the edge case where \( n \geq 2 \); otherwise, it would not enter the loop and simply print 0, which is implied by the loop condition.

