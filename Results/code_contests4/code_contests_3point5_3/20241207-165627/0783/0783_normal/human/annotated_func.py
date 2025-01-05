#State of the program right berfore the function call: n, m, i, j, a, b are all integers such that 1 ≤ n, m ≤ 10^6, 1 ≤ i ≤ n, 1 ≤ j ≤ m, 1 ≤ a, b ≤ 10^6.**
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
        
    #State of the program after the  for loop has been executed: After all iterations of the loop have finished, `n`, `m`, `x`, `y`, `a`, and `b` maintain their original values inputted by the user, and `v` may have been updated based on the conditions within the loop. The final value of `v` depends on the calculations performed in each iteration of the loop.
    if (v and (max(n - x, x - 1) < a or max(m - y, y - 1) < b)) :
        v = 1 << 60
    #State of the program after the if block has been executed: *After the execution of the if-else block, `n`, `m`, `x`, `y`, `a`, and `b` maintain their original values inputted by the user. `v` may have been updated based on the conditions within the loop, and its final value depends on the calculations performed in each iteration of the loop. Upon entering the if condition, `v` is true and `(max(n - x, x - 1) < a or max(m - y, y - 1) < b)` is true. `v` is then assigned the value 1 shifted left by 60 bits.
    print('Poor Inna and pony!', v)[v < 1 << 55]
#Overall this is what the function does:The function `func` reads input values for `n`, `m`, `x`, `y`, `a`, and `b`. It then iterates through a list of coordinates, calculates distances, and updates the value of `v` based on certain conditions. After the loop, it checks a specific condition and may update `v` again. Finally, it prints 'Poor Inna and pony!' followed by the value of `v` if it is less than 1 shifted left by 55 bits. The function does not return any value.

