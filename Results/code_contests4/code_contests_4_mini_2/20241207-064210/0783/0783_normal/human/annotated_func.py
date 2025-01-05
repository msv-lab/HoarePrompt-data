#State of the program right berfore the function call: n and m are positive integers representing the dimensions of the chessboard, i and j are positive integers representing the initial position of the candy on the chessboard such that 1 <= i <= n and 1 <= j <= m, and a and b are positive integers representing the movement offsets.
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
        
    #State of the program after the  for loop has been executed: `n` and `m` are positive integers; `v` is either 0 or the minimum of valid values computed during the iterations based on the conditions applied; `dx` and `dy` are computed as absolute differences between `x`, `y`, and the respective values in `c`.
    if (v and (max(n - x, x - 1) < a or max(m - y, y - 1) < b)) :
        v = 1 << 60
    #State of the program after the if block has been executed: *`n` and `m` are positive integers; `v` is either 0 or 1152921504606846976; `dx` and `dy` are computed as absolute differences between `x`, `y`, and the respective values in `c`. If `v` is non-zero and either the maximum of `n - x` or `x - 1` is less than `a`, or the maximum of `m - y` or `y - 1` is less than `b`, then the conditions for `dx` and `dy` are satisfied based on these calculations.
    print('Poor Inna and pony!', v)[v < 1 << 55]
#Overall this is what the function does:The function accepts positive integers `n` and `m` representing the dimensions of a chessboard, integers `x` and `y` representing the initial position of the candy, and integers `a` and `b` representing movement offsets. It calculates the minimum number of moves required to reach any corner of the chessboard from the initial position based on the specified movement offsets. If it is not possible to reach a corner under the given conditions, it determines that the candy cannot be moved appropriately and returns a message indicating the situation along with a value that reflects the minimum moves calculated. The function also handles cases where the movement is not feasible by checking if the movement offsets exceed the available space in the direction of movement.

