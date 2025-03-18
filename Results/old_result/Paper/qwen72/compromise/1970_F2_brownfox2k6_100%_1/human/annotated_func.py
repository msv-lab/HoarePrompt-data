#State of the program right berfore the function call: obj is a list of two integers representing the coordinates (row, column) of an entity on the field, and d is a string representing the direction of movement ('U', 'D', 'L', or 'R').
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
                #State: *obj is a list of two integers representing the coordinates (row, column) of an entity on the field. If d is 'R', the column value of obj is increased by 1. Otherwise, d is not 'U', 'D', or 'L', and obj remains unchanged.
            #State: *obj is a list of two integers representing the coordinates (row, column) of an entity on the field, and d is a string representing the direction of movement. If d is 'L', the column value of obj is decreased by 1. If d is 'R', the column value of obj is increased by 1. If d is not 'U', 'D', 'L', or 'R', obj remains unchanged.
        #State: *obj is a list of two integers representing the coordinates (row, column) of an entity on the field, and d is a string representing the direction of movement ('D', 'L', 'R', or any other value except 'U'). If d is 'D', the row coordinate of obj is incremented by 1. If d is 'L', the column value of obj is decreased by 1. If d is 'R', the column value of obj is increased by 1. If d is not 'D', 'L', or 'R', obj remains unchanged.
    #State: *`obj` is a list of two integers representing the coordinates (row, column) of an entity on the field, and `d` is a string representing the direction of movement. If `d` is 'U', the row coordinate of `obj` is now `obj[0] - 1` and the column coordinate remains unchanged. If `d` is 'D', the row coordinate of `obj` is incremented by 1. If `d` is 'L', the column coordinate of `obj` is decreased by 1. If `d` is 'R', the column coordinate of `obj` is increased by 1. If `d` is not 'U', 'D', 'L', or 'R', `obj` remains unchanged.
#Overall this is what the function does:The function `func_1` accepts a list `obj` of two integers representing the coordinates (row, column) of an entity on a field, and a string `d` representing the direction of movement ('U', 'D', 'L', or 'R'). It modifies the `obj` list in place to update the coordinates based on the direction: 'U' decreases the row coordinate by 1, 'D' increases the row coordinate by 1, 'L' decreases the column coordinate by 1, and 'R' increases the column coordinate by 1. If `d` is not one of these directions, `obj` remains unchanged. The function does not return any value.

#State of the program right berfore the function call: t is a non-negative integer representing the current time step in the game, and player and blud are dictionaries where the keys are strings representing the players (e.g., 'R0', 'B1') and the values are lists of two integers representing the current coordinates of the players and the Bludger, respectively.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: `t` remains a non-negative integer representing the current time step in the game. `player` is a dictionary where the keys are strings representing the players, and the values are lists of two integers. For any player `p` whose coordinates matched the Bludger's coordinates (`blud`), the coordinates of that player are now `[-1, -1]`. The `out` list contains the keys (player identifiers) of all players whose coordinates matched the Bludger's coordinates.
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: The loop has printed the time step `t` and the player identifier `p` followed by 'ELIMINATED' for each player in the `out` list, in sorted order. The `out` list and the `player` dictionary remain unchanged.
#Overall this is what the function does:The function `func_2` accepts a non-negative integer `t` representing the current time step in the game. It checks if any player's coordinates match the Bludger's coordinates. If a match is found, the player is marked as eliminated by setting their coordinates to `[-1, -1]`, and their identifier is added to a list. The function then prints the time step `t`, the player identifier, and the message 'ELIMINATED' for each eliminated player, in sorted order of the player identifiers. The function does not return any value. After the function concludes, the `player` dictionary is updated with the new coordinates of the eliminated players, and the Bludger's coordinates remain unchanged.

