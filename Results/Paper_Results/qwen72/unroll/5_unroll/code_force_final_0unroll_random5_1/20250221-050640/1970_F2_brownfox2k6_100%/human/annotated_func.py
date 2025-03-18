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
                #State: *obj is a list of two integers representing the coordinates of an entity on the field, and d is a string representing the direction of movement ('U', 'D', 'L', or 'R'). If d is 'R', the second integer in obj is incremented by 1. The direction d is not 'U', not 'D', and not 'L'.
            #State: *`obj` is a list of two integers representing the coordinates of an entity on the field, and `d` is a string representing the direction of movement ('U', 'D', 'L', or 'R'). If `d` is 'L', the second integer in `obj` is decreased by 1. If `d` is 'R', the second integer in `obj` is incremented by 1. The direction `d` is not 'U', not 'D', and retains its original value.
        #State: *`obj` is a list of two integers representing the coordinates of an entity on the field, and `d` is a string representing the direction of movement ('U', 'D', 'L', or 'R'). If `d` is 'D', the first integer in `obj` (obj[0]) is increased by 1. If `d` is 'L', the second integer in `obj` (obj[1]) is decreased by 1. If `d` is 'R', the second integer in `obj` (obj[1]) is incremented by 1. The direction `d` is not 'U' and retains its original value.
    #State: *`obj` is a list of two integers representing the coordinates of an entity on the field, and `d` is a string representing the direction of movement ('U', 'D', 'L', or 'R'). If `d` is 'U', the first integer in `obj` (obj[0]) is decreased by 1. If `d` is 'D', the first integer in `obj` (obj[0]) is increased by 1. If `d` is 'L', the second integer in `obj` (obj[1]) is decreased by 1. If `d` is 'R', the second integer in `obj` (obj[1]) is incremented by 1. The direction `d` retains its original value.
#Overall this is what the function does:The function `func_1` accepts a list `obj` of two integers representing coordinates and a string `d` representing a direction ('U', 'D', 'L', or 'R'). It modifies the coordinates in `obj` based on the direction: 'U' decreases the first coordinate by 1, 'D' increases the first coordinate by 1, 'L' decreases the second coordinate by 1, and 'R' increases the second coordinate by 1. The function does not return any value, but the list `obj` is updated in place. The direction `d` remains unchanged.

#State of the program right berfore the function call: t is a non-negative integer representing the current time step in the game.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: Output State: `t` is a non-negative integer representing the current time step in the game, `out` is a list containing the keys of players that were equal to `blud`, and the values of those players in the `player` dictionary have been set to `[-1, -1]`.
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: `t` is a non-negative integer representing the current time step in the game, `out` is a list containing the keys of players that were equal to `blud`, and the values of those players in the `player` dictionary have been set to `[-1, -1]`. The loop has printed the time step `t`, the player key `p`, and the string 'ELIMINATED' for each player in the sorted `out` list.
#Overall this is what the function does:The function `func_2` accepts a non-negative integer `t` representing the current time step in the game. It identifies players whose values in the `player` dictionary match `blud` and collects their keys into a list `out`. The function then sets the values of these identified players in the `player` dictionary to `[-1, -1]`. Finally, it prints the time step `t`, the player key, and the string 'ELIMINATED' for each player in the sorted `out` list. The function does not return any value.

