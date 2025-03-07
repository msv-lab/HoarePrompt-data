#State of the program right berfore the function call: a is a 2D list representing the field, where each element is a string of length 2 indicating the presence of a player, a goal, the Quaffle, a Bludger, or an empty cell. b is an integer representing the number of steps in the game.
def func_1(a, b):
    x, y = a
    dx, dy = b
    return x + dx, y + dy
    #The program returns x + b, y + b
#Overall this is what the function does:The function accepts a 2D list `a` (though it is not used in the function) and an integer `b`. It returns new coordinates `(x + b, y + b)` by shifting the original coordinates `(x, y)` by `b` in both dimensions.

