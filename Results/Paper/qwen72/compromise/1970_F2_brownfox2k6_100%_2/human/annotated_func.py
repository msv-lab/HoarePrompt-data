#State of the program right berfore the function call: obj is a list of two integers representing the coordinates of an entity on the field, and d is a string representing the direction of movement ('U', 'D', 'L', 'R').
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
                #State: *`obj` is a list of two integers representing the coordinates of an entity on the field. If `d` is 'R', the second integer in `obj` is incremented by 1. Otherwise, `d` is not 'U', 'D', or 'L', and `obj` remains unchanged.
            #State: *`obj` is a list of two integers representing the coordinates of an entity on the field, and `d` is a string representing the direction of movement. If `d` is 'L', the second integer in `obj` is decreased by 1. If `d` is 'R', the second integer in `obj` is incremented by 1. Otherwise, if `d` is not 'U', 'D', 'L', or 'R', `obj` remains unchanged.
        #State: *`obj` is a list of two integers representing the coordinates of an entity on the field, and `d` is a string representing the direction of movement ('D', 'L', 'R', or an invalid direction). If `d` is 'D', the first integer in `obj` is incremented by 1. If `d` is 'L', the second integer in `obj` is decreased by 1. If `d` is 'R', the second integer in `obj` is incremented by 1. If `d` is not 'U', 'D', 'L', or 'R', `obj` remains unchanged.
    #State: *`obj` is a list of two integers representing the coordinates of an entity on the field, and `d` is a string representing the direction of movement ('U', 'D', 'L', 'R', or an invalid direction). If `d` is 'U', the first integer in `obj` is decreased by 1. If `d` is 'D', the first integer in `obj` is incremented by 1. If `d` is 'L', the second integer in `obj` is decreased by 1. If `d` is 'R', the second integer in `obj` is incremented by 1. If `d` is not 'U', 'D', 'L', or 'R', `obj` remains unchanged.
#Overall this is what the function does:The function `func_1` accepts a list `obj` of two integers representing coordinates and a string `d` representing a direction ('U', 'D', 'L', 'R'). It modifies the coordinates in `obj` based on the direction: if `d` is 'U', the first integer is decreased by 1; if `d` is 'D', the first integer is increased by 1; if `d` is 'L', the second integer is decreased by 1; if `d` is 'R', the second integer is increased by 1. If `d` is not one of these directions, `obj` remains unchanged. The function does not return any value.

#State of the program right berfore the function call: t is a non-negative integer representing the current time step in the game.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: Output State: `t` is a non-negative integer representing the current time step in the game, `out` is a list containing the keys of players that were equal to `blud`, and `player` is a dictionary where the values of the keys that were equal to `blud` have been set to `[-1, -1]`.
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: The value of `t` remains a non-negative integer representing the current time step in the game. The list `out` remains unchanged, containing the keys of players that were equal to `blud`. The dictionary `player` remains unchanged, with the values of the keys that were equal to `blud` set to `[-1, -1]`. The loop prints the time step `t`, the player key `p`, and the string 'ELIMINATED' for each player in `out`, but does not modify any of the variables in the loop head or body.
#Overall this is what the function does:The function `func_2` accepts a non-negative integer `t` representing the current time step in the game. It identifies players in the `player` dictionary whose values match `blud` and updates their values to `[-1, -1]`. It then prints a message for each of these players, indicating the time step and that the player has been eliminated. The function does not return any value. After the function concludes, the `player` dictionary will have the values of the identified players set to `[-1, -1]`, and the time step `t` remains unchanged.

