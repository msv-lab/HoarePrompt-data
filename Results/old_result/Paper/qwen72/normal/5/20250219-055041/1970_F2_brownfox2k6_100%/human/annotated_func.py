#State of the program right berfore the function call: obj is a list of two integers representing the coordinates of an entity on the field, and d is a string representing the direction of movement, which can be 'U', 'D', 'L', or 'R'.
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
                #State: *obj is a list of two integers representing the coordinates of an entity on the field, and the second integer in obj is increased by 1, d is 'R'.
            #State: *obj is a list of two integers representing the coordinates of an entity on the field. If d is 'L', the second integer (y-coordinate) in obj is decreased by 1. If d is 'R', the second integer (y-coordinate) in obj is increased by 1.
        #State: `obj` is a list of two integers representing the coordinates of an entity on the field. If `d` is 'D', the first integer (x-coordinate) in `obj` is incremented by 1. If `d` is 'L', the second integer (y-coordinate) in `obj` is decreased by 1. If `d` is 'R', the second integer (y-coordinate) in `obj` is increased by 1.
    #State: *`obj` is a list of two integers representing the coordinates of an entity on the field. If `d` is 'U', the first integer (x-coordinate) in `obj` is decreased by 1. If `d` is 'D', the first integer (x-coordinate) in `obj` is incremented by 1. If `d` is 'L', the second integer (y-coordinate) in `obj` is decreased by 1. If `d` is 'R', the second integer (y-coordinate) in `obj` is increased by 1.
#Overall this is what the function does:The function `func_1` accepts a list `obj` of two integers representing coordinates and a string `d` representing a direction ('U', 'D', 'L', 'R'). It modifies the coordinates in `obj` based on the direction: if `d` is 'U', the x-coordinate is decreased by 1; if `d` is 'D', the x-coordinate is increased by 1; if `d` is 'L', the y-coordinate is decreased by 1; if `d` is 'R', the y-coordinate is increased by 1. The function does not return any value, but the list `obj` is updated with the new coordinates.

#State of the program right berfore the function call: t is a non-negative integer representing the current step in the game.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: `t` is a non-negative integer, `out` is a list containing all the keys from `player` whose values were equal to `blud` before the loop started, and the values of these keys in `player` are now `[-1, -1]`. The values of other keys in `player` that were not equal to `blud` remain unchanged.
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: `t` is a non-negative integer, `out` is an empty list, and the values of the keys in `player` that were equal to `blud` before the loop started are now `[-1, -1]`. The values of other keys in `player` that were not equal to `blud` remain unchanged.
#Overall this is what the function does:The function `func_2` accepts a non-negative integer `t` representing the current step in the game. It identifies all players in the `player` dictionary whose values match `blud` and updates their values to `[-1, -1]`. It then prints a message for each of these players, indicating that they have been eliminated at step `t`. The function does not return any value. After the function concludes, the `player` dictionary will have the values of the eliminated players set to `[-1, -1]`, and the values of other players remain unchanged.

