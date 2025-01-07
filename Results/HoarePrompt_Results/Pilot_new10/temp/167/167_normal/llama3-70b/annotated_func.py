#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200000, and a is a list of integers of length n where each integer a_i is between 1 and 10^9.
def func_1(x, y):
    px, py = 0, 0
    for v in a:
        nx, ny = (v - 1) // y, (v - 1) % y
        
        if abs(nx - px) + abs(ny - py) != 1:
            return False
        
        px, py = nx, ny
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 200000, `a` is a list of integers of length `n`, `px` is (a[n-1] - 1) // y, `py` is (a[n-1] - 1) % y, `v` is the last element in the list `a`, `nx` is (a[n-1] - 1) // y, `ny` is (a[n-1] - 1) % y.
    return True
    #The program returns True
#Overall this is what the function does:The function accepts an integer `x` and a list of integers `a`. It checks if the coordinates derived from each element in `a` can be traversed sequentially in a grid-like manner, returning False if the moves between successive elements are not valid (i.e., not adjacent), and True if all moves are valid.

