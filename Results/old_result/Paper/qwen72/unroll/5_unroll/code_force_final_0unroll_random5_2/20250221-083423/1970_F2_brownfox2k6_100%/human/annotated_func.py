#State of the program right berfore the function call: obj is a list of two integers representing the coordinates of an entity on the field, and d is a string representing the direction ('U', 'D', 'L', 'R') in which the entity will move. The coordinates in obj must be within the bounds of the field defined by N and M, and the move should not result in the entity moving outside these bounds.
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
                #State: *`obj` is a list of two integers representing the coordinates of an entity on the field, and `d` is a string representing the direction ('R'). If `d` is 'R', the coordinates in `obj` are now (obj[0], obj[1] + 1), and the move should not result in the entity moving outside the bounds defined by N and M. The direction `d` is not 'U', the direction `d` is not 'D', and the direction `d` is not 'L'. If `d` is not 'R', the coordinates in `obj` remain unchanged.
            #State: *`obj` is a list of two integers representing the coordinates of an entity on the field, and `d` is a string representing the direction ('L', 'R'). If `d` is 'L', the second integer (y-coordinate) in `obj` is decreased by 1, and the move should not result in the entity moving outside the bounds defined by N and M. If `d` is 'R', the second integer (y-coordinate) in `obj` is increased by 1, and the move should not result in the entity moving outside the bounds defined by N and M. If `d` is neither 'L' nor 'R', the coordinates in `obj` remain unchanged. The direction `d` is not 'U', and the direction `d` is not 'D'.
        #State: *`obj` is a list of two integers representing the coordinates of an entity on the field, and `d` is a string representing the direction ('L', 'R', 'D'). If `d` is 'D', the first coordinate of `obj` is increased by 1, and the move does not result in the entity moving outside the bounds defined by N and M. If `d` is 'L', the second integer (y-coordinate) in `obj` is decreased by 1, and the move should not result in the entity moving outside the bounds defined by N and M. If `d` is 'R', the second integer (y-coordinate) in `obj` is increased by 1, and the move should not result in the entity moving outside the bounds defined by N and M. If `d` is neither 'L' nor 'R', the coordinates in `obj` remain unchanged. The direction `d` is not 'U'.
    #State: *`obj` is a list of two integers representing the coordinates of an entity on the field, and `d` is a string representing the direction ('U', 'D', 'L', 'R'). If `d` is 'U', the first integer in `obj` is decreased by 1. If `d` is 'D', the first integer in `obj` is increased by 1. If `d` is 'L', the second integer in `obj` is decreased by 1. If `d` is 'R', the second integer in `obj` is increased by 1. In all cases, the move does not result in the entity moving outside the bounds defined by N and M. If `d` is neither 'U', 'D', 'L', nor 'R', the coordinates in `obj` remain unchanged.
#Overall this is what the function does:The function `func_1` accepts a list `obj` of two integers representing the coordinates of an entity on a field and a string `d` representing a direction ('U', 'D', 'L', 'R'). It modifies the coordinates in `obj` based on the direction: 'U' decreases the x-coordinate by 1, 'D' increases the x-coordinate by 1, 'L' decreases the y-coordinate by 1, and 'R' increases the y-coordinate by 1. The function does not return any value, but the coordinates in `obj` are updated in place. The function assumes that the move will not result in the entity moving outside the bounds defined by N and M, and if `d` is not one of the specified directions, the coordinates in `obj` remain unchanged.

#State of the program right berfore the function call: t is a non-negative integer representing the current time step in the game, and `player` and `blud` are dictionaries where the keys are strings representing player identifiers (e.g., 'R0', 'B1') and the values are lists of integers representing the current position of the player or the Bludger on the field. The positions are valid and within the bounds of the field.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: `t` remains unchanged, `player` has the positions of any players that matched the Bludger's position updated to `[-1, -1]`, and `out` contains the identifiers of those players.
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: The loop prints the value of `t` and each player identifier in `out` in ascending order, followed by 'ELIMINATED'. The variables `t`, `player`, and `out` remain unchanged.
#Overall this is what the function does:The function `func_2` accepts a non-negative integer `t` and two dictionaries `player` and `blud`. It checks if any player's position matches the Bludger's position. If a match is found, the player's position is updated to `[-1, -1]` (indicating elimination), and the player's identifier is added to a list `out`. The function then prints the time step `t` and each player identifier in `out` in ascending order, followed by 'ELIMINATED'. The function does not return any value. After the function concludes, `t` remains unchanged, `player` has the positions of any eliminated players updated to `[-1, -1]`, and `out` contains the identifiers of the eliminated players.

