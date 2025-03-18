#State of the program right berfore the function call: x and y are positive integers such that 1 <= x, y <= 10^9, and a list of integers numbers where 1 <= a_i <= 10^9 for all 1 <= i <= n, representing the sequence of integers in the cells visited on the path.
def func_1(x, y):
    px, py = 0, 0
    for v in a:
        nx, ny = (v - 1) // y, (v - 1) % y
        
        if abs(nx - px) + abs(ny - py) != 1:
            return False
        
        px, py = nx, ny
        
    #State of the program after the  for loop has been executed: 
    return True
    #The program returns True
#Overall this is what the function does:The function accepts two positive integers `x` and `y`, and a list of integers `a`. It returns `True` if the sequence of cells represented by the integers in `a` forms a valid path on a grid of size `x` by `y` where each step moves to an adjacent cell. If any step is invalid, it returns `False`.

