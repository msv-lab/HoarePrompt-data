#State of the program right berfore the function call: n, m, i, j, a, b are all integers such that 1 <= n, m, i, j, a, b <= 10^6.**
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
        
    #State of the program after the  for loop has been executed: `n` and `m` are integers such that 1 <= n, m <= 10^6. `v` will be updated based on the conditions specified in the loop code. The final value of `v` will be the minimum value obtained from all iterations of the loop.
    if (v and (max(n - x, x - 1) < a or max(m - y, y - 1) < b)) :
        v = 1 << 60
    #State of the program after the if block has been executed: *`n` and `m` are integers such that 1 <= n, m <= 10^6. `v` will be updated based on the conditions specified in the loop code. The final value of `v` will be the minimum value obtained from all iterations of the loop. If `v` and (max(n - x, x - 1) < a or max(m - y, y - 1) < b) is true, then `v` is assigned the value 1 << 60.
    print('Poor Inna and pony!', v)[v < 1 << 55]
#Overall this is what the function does:The function reads integers n, m, x, y, a, b, and performs calculations to determine the minimum value of a certain expression. It then checks conditions and prints a message accordingly. If the calculated minimum value is less than a specific threshold, it prints 'Poor Inna and pony!'. However, there might be potential cases where the function does not behave as expected based on the annotations, such as the handling of edge cases related to the conditions in the loop.

