#State of the program right berfore the function call: n, m, i, j, a, and b are integers such that 1 ≤ n, m, i ≤ n, j ≤ m, and 1 ≤ a, b.
def func():
    n, m, x, y, a, b = map(int, raw_input().split())
    v = 1 << 60
    for c in [(1, m), (n, 1), (n, m), (1, 1)]:
        dx = abs(x - c[0])
        
        dy = abs(y - c[1])
        
        if 0 == dx + dy:
            v = 0
        elif dx % a == 0 and dy % b == 0 and dx / a % 2 == dy / b % 2:
            v = min(v, max(dx / a, dy / b))
        
    #State of the program after the  for loop has been executed: `n`, `m`, `i`, `j`, `a`, and `b` are integers; `x` and `y` are integers from input; `v` is the minimum of its initial value (1152921504606846976) and the maximum values computed from the valid conditions based on the absolute differences between `x`, `y`, and the coordinates in `c`, if any valid conditions were satisfied. If any coordinate matches `x` and `y`, then `v` is set to 0.
    if (v and (max(n - x, x - 1) < a or max(m - y, y - 1) < b)) :
        v = 1 << 60
    #State of the program after the if block has been executed: *`n`, `m`, `i`, `j`, `a`, and `b` are integers; `x` and `y` are integers from input; if `v` is non-zero and the maximum of `n - x` or `x - 1` is less than `a`, or the maximum of `m - y` or `y - 1` is less than `b`, then `v` is set to 1 << 60. Otherwise, `v` retains its value, which is the minimum of its initial value (1152921504606846976) and the maximum values computed from the valid conditions based on the absolute differences between `x`, `y`, and the coordinates in `c`, with the possibility of being set to 0 if any coordinate matches `x` and `y`.
    print('Poor Inna and pony!', v)[v < 1 << 55]
#Overall this is what the function does:The function accepts six integer parameters: n, m, x, y, a, and b, where 1 ≤ n, m, x ≤ n, y ≤ m, and 1 ≤ a, b. It calculates a value v based on the distance from (x, y) to four corners of a grid defined by (1, 1), (1, m), (n, 1), and (n, m). If the distance can be evenly divided by a and b, and the resulting ratios have the same parity, it updates v to the maximum of the two ratios. If (x, y) matches any corner, v is set to 0. If certain conditions on the maximum distances to the edges of the grid are met, v is reset to its initial large value. The function finally prints 'Poor Inna and pony!' followed by v if v is less than 1 << 55; otherwise, it prints nothing.

