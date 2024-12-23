#State of the program right berfore the function call: n is a positive integer, the sequence is a string of n characters from 'U', 'D', 'L', 'R', and x and y are integers.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer, `ops` is a string input by the user, `x` and `y` are input integers, `lx` is 0, `ly` is 0, `ux` is the difference between the number of 'R' and 'L' operations in `ops`, `uy` is the difference between the number of 'U' and 'D' operations in `ops`.
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
            
        #State of the program after the  for loop has been executed: `n` is an input integer, `ops` is a string input by the user, `x` is an input integer, `y` is an input integer, `lx` is 0, `ly` is 0, `ux` is the difference between the number of 'R' and 'L' operations in `ops`, `uy` is the difference between the number of 'U' and 'D' operations in `ops`, `dx` is either 0 or the difference between `x` and `ux` if all 'R' operations did not reduce `dx` to 0, `dy` is either 0 or the difference between `y` and `uy` if all 'U' operations did not reduce `dy` to 0, `res` is the total number of operations that did not change `dx` or `dy`.
        print(res)
    #State of the program after the if-else block has been executed: `n` is an input integer, `ops` is a string input by the user, `x` is an input integer, `y` is an input integer, `lx` is 0, `ly` is 0, `ux` is the difference between the number of 'R' and 'L' operations in `ops`, `uy` is the difference between the number of 'U' and 'D' operations in `ops`, `dx` is `x - ux`, `dy` is `y - uy`. If `dx` is less than 0 or `dy` is less than 0, the function returns -1. Otherwise, `dx` is either 0 or the difference between `x` and `ux` if all 'R' operations did not reduce `dx` to 0, `dy` is either 0 or the difference between `y` and `uy` if all 'U' operations did not reduce `dy` to 0, and the function returns `res`, which is the total number of operations that did not change `dx` or `dy`.
#Overall this is what the function does:The function accepts parameters n, sequence, x, and y, where n is a positive integer, sequence is a string of n characters from 'U', 'D', 'L', 'R', and x and y are integers. It calculates the net movement in the x and y directions based on the sequence of operations. If the target position (x, y) is not reachable after executing all operations (i.e., x - net x movement < 0 or y - net y movement < 0), the function returns -1. Otherwise, it counts the number of operations that do not change the difference between the target position and the current position (i.e., the operations that are not necessary to reach the target position) and returns this count. The function effectively measures the number of redundant operations in the sequence with respect to reaching the target position (x, y).

