#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 200000, a is a list of n integers where each integer a[i] satisfies 1 ≤ a[i] ≤ 10^9.
def func_1(x, y):
    px, py = 0, 0
    for v in a:
        nx, ny = (v - 1) // y, (v - 1) % y
        
        if abs(nx - px) + abs(ny - py) != 1:
            return False
        
        px, py = nx, ny
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 200000, `a` is a list of `n` integers, `px` is equal to the last computed `nx`, `py` is equal to the last computed `ny`.
    return True
    #The program returns True
#Overall this is what the function does:The function accepts two integer parameters `x` and `y`, and iterates through a global list `a`. It calculates `nx` and `ny` based on each element `v` in `a`. If the absolute difference between the current and previous computed positions `(nx, ny)` and `(px, py)` is not equal to 1, it returns False. If all elements in `a` are processed without violating this condition, it returns True. Therefore, the function checks if the elements in the list can represent a valid movement in a grid defined by `x` and `y`.

