#State of the program right berfore the function call: obj is a list of two integers representing the coordinates of an entity on the field, and d is a string representing the direction of movement ('U', 'D', 'L', or 'R').
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
                #State: `obj` is a list of two integers representing the coordinates of an entity on the field. If `d` is 'R', the second integer (y-coordinate) in `obj` is increased by 1. Otherwise, `obj` remains unchanged, and `d` is not 'U', 'D', or 'L'.
            #State: *`obj` is a list of two integers representing the coordinates of an entity on the field, and `d` is a string representing the direction of movement ('U', 'D', 'L', or 'R'). If `d` is 'L', the second element of `obj` is decreased by 1. If `d` is 'R', the second element of `obj` is increased by 1. Otherwise, `obj` remains unchanged, and `d` is not 'U', 'D', or 'L'.
        #State: *`obj` is a list of two integers representing the coordinates of an entity on the field, and `d` is a string representing the direction of movement ('U', 'D', 'L', or 'R'). If `d` is 'D', the first element of `obj` is increased by 1. If `d` is 'L', the second element of `obj` is decreased by 1. If `d` is 'R', the second element of `obj` is increased by 1. Otherwise, `obj` remains unchanged, and `d` is not 'U', 'D', or 'L'.
    #State: *`obj` is a list of two integers representing the coordinates of an entity on the field, and `d` is a string representing the direction of movement ('U', 'D', 'L', or 'R'). If `d` is 'U', the first integer in `obj` is decreased by 1. If `d` is 'D', the first integer in `obj` is increased by 1. If `d` is 'L', the second integer in `obj` is decreased by 1. If `d` is 'R', the second integer in `obj` is increased by 1. Otherwise, `obj` remains unchanged.
#Overall this is what the function does:The function `func_1` accepts a list `obj` of two integers representing coordinates and a string `d` representing a direction ('U', 'D', 'L', or 'R'). It modifies the coordinates in `obj` based on the direction: if `d` is 'U', the first integer (x-coordinate) is decreased by 1; if `d` is 'D', the first integer is increased by 1; if `d` is 'L', the second integer (y-coordinate) is decreased by 1; if `d` is 'R', the second integer is increased by 1. The function does not return any value, but the final state of `obj` reflects the new coordinates after the movement.

#State of the program right berfore the function call: t is a non-negative integer representing the current time step in the game.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: Output State: `t` is a non-negative integer representing the current time step in the game, `out` is a list containing the keys (player IDs) of players that were equal to `blud`, and the values of these players in the `player` dictionary have been set to `[-1, -1]`. The state of `t` remains unchanged.
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: The value of `t` remains unchanged, and the list `out` contains the player IDs that were equal to `blud`. The values of these players in the `player` dictionary have been set to `[-1, -1]`. The loop prints the current time step `t`, the player ID `p`, and the string 'ELIMINATED' for each player ID in `out`, in ascending order.
#Overall this is what the function does:The function `func_2` accepts a non-negative integer `t` representing the current time step in the game. It identifies players in the `player` dictionary whose values match `blud` and sets their values to `[-1, -1]`. It returns nothing but prints the current time step `t`, the player ID, and the string 'ELIMINATED' for each identified player, in ascending order of player IDs. The value of `t` remains unchanged throughout the function execution.

