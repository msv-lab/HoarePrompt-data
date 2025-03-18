#State of the program right berfore the function call: obj is a list containing two integers representing the coordinates (row, column) of an entity on the field, and d is a string representing the direction of movement ('U', 'D', 'L', 'R').
def func_1(obj, d):
    if (d == 'U') :
        obj[0] -= 1
    else :
        if (d == 'D') :
            obj[0] += 1
        else :
            if (d == 'L') :
                obj[1] -= 1
            else :
                if (d == 'R') :
                    obj[1] += 1
                #State: `obj` is a list containing two integers representing the coordinates (row, column) of an entity on the field. If `d` is 'R', the column value in `obj` has been incremented by 1. If `d` is not 'R', the coordinates in `obj` remain unchanged.
            #State: `obj` is a list containing two integers representing the coordinates (row, column) of an entity on the field. If `d` is 'L', the column coordinate has been decremented by 1. If `d` is 'R', the column coordinate has been incremented by 1. If `d` is neither 'L' nor 'R', the coordinates in `obj` remain unchanged.
        #State: `obj` is a list containing two integers representing the coordinates (row, column) of an entity on the field. If `d` is 'D', the row coordinate has been incremented by 1. If `d` is 'L', the column coordinate has been decremented by 1. If `d` is 'R', the column coordinate has been incremented by 1. If `d` is neither 'D', 'L', nor 'R', the coordinates in `obj` remain unchanged.
    #State: `obj` is a list containing two integers representing the coordinates (row, column) of an entity on the field. If `d` is 'U', the row coordinate is decreased by 1. If `d` is 'D', the row coordinate is incremented by 1. If `d` is 'L', the column coordinate is decremented by 1. If `d` is 'R', the column coordinate is incremented by 1. If `d` is neither 'U', 'D', 'L', nor 'R', the coordinates in `obj` remain unchanged.
#Overall this is what the function does:The function `func_1` updates the coordinates of an entity on a field based on the specified direction of movement ('U' for up, 'D' for down, 'L' for left, 'R' for right). The function modifies the input list `obj` in place to reflect the new coordinates after the movement. If the direction is not one of the specified valid directions, the coordinates remain unchanged.

#State of the program right berfore the function call: t is a non-negative integer representing the current time step, player is a dictionary where keys are player identifiers (strings) and values are lists of two integers representing their positions on the field, and blud is a list of two integers representing the position of the Bludger on the field.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: `t` is a non-negative integer representing the current time step, `player` is a dictionary where keys are player identifiers (strings) and values are lists of two integers representing their positions on the field, with any player who was at the same position as the Bludger having their position updated to `[-1, -1]`, `blud` is a list of two integers representing the position of the Bludger on the field, and `out` is a list containing the identifiers of players who were at the same position as the Bludger.`
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: `t` is a non-negative integer representing the current time step, `player` is a dictionary where keys are player identifiers (strings) and values are lists of two integers representing their positions on the field, with any player who was at the same position as the Bludger having their position updated to `[-1, -1]`, `blud` is a list of two integers representing the position of the Bludger on the field, and `out` is a list containing the identifiers of players who were at the same position as the Bludger.
#Overall this is what the function does:The function checks if any player is at the same position as the Bludger. If a player is found at the Bludger's position, their position is updated to `[-1, -1]`, and their identifier is printed along with the current time step and the message 'ELIMINATED'.

