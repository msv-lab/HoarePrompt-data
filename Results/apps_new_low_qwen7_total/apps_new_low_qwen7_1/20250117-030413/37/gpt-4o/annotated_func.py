#State of the program right berfore the function call: n is an integer such that 0 <= n <= 10^18.
def func_1(n):
    directions = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]

x, y = 0, 0

steps = 1

direction_index = 0
    while n > 0:
        for _ in range(2):
            if n >= steps:
                dx, dy = directions[direction_index]
                x += dx * steps
                y += dy * steps
                n -= steps
                direction_index = (direction_index + 1) % 6
            else:
                dx, dy = directions[direction_index]
                x += dx * n
                y += dy * n
                return x, y
        
        steps += 1
        
    #State of the program after the loop has been executed: \( n \leq 0 \), \( steps \) is the last value before \( n \) became non-positive, \( direction_index = (original direction_index + 2 \times k) \% 6 \), \( x = x_{initial} + 8 \times (dx_1 + dx_2 + \ldots + dx_k) + n \times dx \), \( y = y_{initial} + 8 \times (dy_1 + dy_2 + \ldots + dy_k) + n \times dy \)
    return x, y
    #The program returns x and y, where \( x = x_{initial} + 8 \times (dx_1 + dx_2 + \ldots + dx_k) + n \times dx \) and \( y = y_{initial} + 8 \times (dy_1 + dy_2 + \ldots + dy_k) + n \times dy \)
#Overall this is what the function does:The function `func_1` accepts an integer `n` as input and returns the updated coordinates `(x, y)`. The function uses a set of predefined movement directions to update the coordinates `x` and `y` based on the value of `n`. Specifically, it updates `x` and `y` by moving in different directions depending on the current step count and the remaining value of `n`. If `n` is greater than or equal to the current step size, it moves in a full step in the current direction. Otherwise, it performs a partial step and then exits the function. After exiting the loop, the function returns the final coordinates `(x, y)` based on the accumulated movements.

