#State of the program right berfore the function call: n, m, i, j, a, b are integers such that 1 <= n, m, i, j, a, b <= 10^6.**
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
        
    #State of the program after the  for loop has been executed: `n`, `m`, `x`, `y`, `a`, `b`, `v` remain unchanged. If `dx` is divisible by `a` and `dy` is divisible by `b`, and the quotient of `dx` divided by `a` has the same parity as the quotient of `dy` divided by `b`, then no changes are made to any variables. Otherwise, `v` remains the same as the minimum value of the current `v` and the maximum value of the quotients `dx / a` and `dy / b`.
    if (v and (max(n - x, x - 1) < a or max(m - y, y - 1) < b)) :
        v = 1 << 60
    #State of the program after the if block has been executed: *`n`, `m`, `x`, `y`, `a`, `b` remain unchanged. If `dx` is divisible by `a` and `dy` is divisible by `b`, and the quotient of `dx` divided by `a` has the same parity as the quotient of `dy` divided by `b`, then no changes are made to any variables. Otherwise, `v` remains the same as the minimum value of the current `v` and the maximum value of the quotients `dx / a` and `dy / b`. If `v` and the maximum of the absolute differences between `n` and `x`, `m` and `y` with `a` and `b` respectively is less than `a` and `b` respectively, then `v` retains the minimum value of the current `v` and the maximum of the quotients `dx / a` and `dy / b`.
    print('Poor Inna and pony!', v)[v < 1 << 55]
#Overall this is what the function does:The function `func` reads input integers `n`, `m`, `x`, `y`, `a`, `b` and calculates a value `v` based on certain conditions involving these input values. It iterates through different coordinate pairs, calculates distances, and updates the value of `v` accordingly. At the end, it checks `v` against certain conditions and prints a message based on the value of `v`. The function does not have a return value.

