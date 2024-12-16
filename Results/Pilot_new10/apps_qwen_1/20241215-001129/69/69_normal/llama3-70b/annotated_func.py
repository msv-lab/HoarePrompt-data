#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, the string consists of 'U', 'D', 'L', and 'R' characters representing operations, and x, y are integers such that -10^9 ≤ x, y ≤ 10^9.
def func():
    n = int(input())
    ops = input()
    x, y = map(int, input().split())
    ux, uy, lx, ly = 0, 0, 0, 0
    for op in ops:
        if op == 'U':
            uy += 1
        elif op == 'D':
            uy -= 1
        elif op == 'R':
            ux += 1
        elif op == 'L':
            ux -= 1
        
    #State of the program after the  for loop has been executed: `ops` is a non-empty string, `uy` is the net change in the y-coordinate (initially 0), `ux` is the net change in the x-coordinate (initially 0).
    dx, dy = x - ux, y - uy
    if (dx < 0 or dy < 0) :
        print(-1)
    else :
        res = 0
        for op in ops:
            if op == 'U' and dy > 0:
                dy -= 1
            elif op == 'D' and dy < 0:
                dy += 1
            elif op == 'R' and dx > 0:
                dx -= 1
            elif op == 'L' and dx < 0:
                dx += 1
            else:
                res += 1
            
        #State of the program after the  for loop has been executed: `ops` is a non-empty string, `ux` is 0, `uy` is 0, `dx` is the final horizontal displacement, `dy` is the final vertical displacement, `res` is the count of operations that did not affect `dx` or `dy`.
        print(res)
    #State of the program after the if-else block has been executed: *`ops` is a non-empty string, `ux` is 0, `uy` is 0. If `dx < 0` or `dy < 0`, then -1 is printed to the console. Otherwise, `dx` is the final horizontal displacement, `dy` is the final vertical displacement, and `res` is the count of operations that did not affect `dx` or `dy`.
#Overall this is what the function does:The function processes a string of operations ('U', 'D', 'L', 'R') and two integers `x` and `y` to determine the final position after performing the operations. If the final coordinates (x, y) are negative, it prints -1. Otherwise, it counts and returns the number of operations that did not affect the final coordinates (x, y).

