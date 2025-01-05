#State of the program right berfore the function call: n, m, i, j, a, and b are integers such that 1 ≤ n, m ≤ 10^6, 1 ≤ i ≤ n, 1 ≤ j ≤ m, and 1 ≤ a, b ≤ 10^6.
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
        
    #State of the program after the  for loop has been executed: `v` is the minimum of its initial value and the maximum of (`dx / a`, `dy / b`) for each condition met, where `c` takes values from [(1, m), (n, 1), (n, m), (1, 1)]. `dx` and `dy` are calculated as abs(x - c[0]) and abs(y - c[1]) respectively. If any of the conditions are not met during any iteration, `v` will remain unchanged from its initial value.
    if (v and (max(n - x, x - 1) < a or max(m - y, y - 1) < b)) :
        v = 1 << 60
    #State of the program after the if block has been executed: *`v` is the minimum of its initial value and the maximum of (`dx / a`, `dy / b`) for each condition met. If `v` is `1 << 60` and either `max(n - x, x - 1) < a` or `max(m - y, y - 1) < b` holds true, then `v` remains `1 << 60`. If the conditions are not met, `v` will remain unchanged from its initial value.
    print('Poor Inna and pony!', v)[v < 1 << 55]
#Overall this is what the function does:The function reads six integers from input, representing dimensions and coordinates, calculates a value based on specific conditions related to distances from corners of a rectangle, and prints a message along with the computed value if it meets certain criteria. If the conditions for computing the value are not met, it defaults to a large initial value. However, it does not return any value explicitly but rather prints the result. The function appears to handle edge cases for distance calculations and checks but does not have any defined output for cases where all conditions fail.

