#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 2 ⋅ 10^5, the sequence of operations is a string consisting of 'U', 'D', 'L', and 'R' characters, and the target coordinates (x, y) are integers such that -10^9 ≤ x, y ≤ 10^9.
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
        
    #State of the program after the  for loop has been executed: `ops` is a non-empty string, `ux` is the final x-coordinate after processing all operations in `ops`, `uy` is the final y-coordinate after processing all operations in `ops`.
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
            
        #State of the program after the  for loop has been executed: `dx` is the net horizontal displacement, `dy` is the net vertical displacement, `ops` is the original operations string, `ux` is `x - dx`, `uy` is `y - dy`, `res` is the count of invalid operations.
        print(res)
    #State of the program after the if-else block has been executed: `dx` is `x - ux`, `dy` is `y - uy`, `ops` is a non-empty string, `ux` is the final x-coordinate after processing all operations in `ops`, `uy` is the final y-coordinate after processing all operations in `ops`. If `dx < 0` or `dy < 0`, the function prints `-1`. Otherwise, `ux` is updated to `x - dx`, `uy` is updated to `y - dy`, `res` is the count of invalid operations.
#Overall this is what the function does:The function `func()` takes a sequence of operations (`ops`) as a string and two integer coordinates `(x, y)` as inputs. It calculates the final coordinates `(ux, uy)` after processing the operations and then checks if these new coordinates can be reached from the original coordinates `(x, y)` by performing the same operations. If the new coordinates cannot be reached, the function prints `-1`. Otherwise, it counts the number of invalid operations (those that would not help in reaching the target coordinates) and prints this count.

