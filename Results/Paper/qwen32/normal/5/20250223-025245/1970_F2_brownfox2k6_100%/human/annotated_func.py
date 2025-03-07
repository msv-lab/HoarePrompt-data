#State of the program right berfore the function call: obj is a list containing two integers representing the coordinates (row, column) of an entity on the field, and d is a string representing a direction ('U', 'D', 'L', 'R') indicating the movement to be performed by the entity.
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
                #State: `obj` is a list containing two integers representing the coordinates (row, column) of an entity on the field. If `d` is 'R', the column has been incremented by 1. Since `d` is not 'U', 'D', or 'L', no other changes occur to `obj` or `d`.
            #State: `obj` is a list containing two integers representing the coordinates (row, column) of an entity on the field. If `d` is 'L', the column value is decreased by 1. If `d` is 'R', the column value is increased by 1. Since `d` is not 'U' or 'D', no other changes occur to `obj` or `d`.
        #State: `obj` is a list containing two integers representing the coordinates (row, column) of an entity on the field. If `d` is 'D', the row coordinate is incremented by 1. If `d` is 'L', the column value is decreased by 1. If `d` is 'R', the column value is increased by 1. Since `d` is not 'U', no other changes occur to `obj` or `d`.
    #State: `obj` is a list containing two integers representing the coordinates (row, column) of an entity on the field. If `d` is 'U', the row coordinate is one less than its initial value. If `d` is 'D', the row coordinate is incremented by 1. If `d` is 'L', the column value is decreased by 1. If `d` is 'R', the column value is increased by 1.
#Overall this is what the function does:The function `func_1` updates the coordinates of an entity on a field based on a specified direction ('U', 'D', 'L', 'R'). It modifies the input list `obj` to reflect the new coordinates after moving the entity in the indicated direction.

#State of the program right berfore the function call: t is a non-negative integer representing the current time step, player is a dictionary where keys are player identifiers (strings in the format "R0", "B0", ..., "R9", "B9") and values are lists of two integers representing the player's position on the field, and blud is a list of two integers representing the position of the Bludger on the field.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: `t` is a non-negative integer representing the current time step, `player` is a dictionary where `player[p]` is `[-1, -1]` if `player[p]` was equal to `blud` at any point during the loop, otherwise `player[p]` remains unchanged, `blud` is a list of two integers representing the position of the Bludger on the field, and `out` is a list containing the values of all player identifiers `p` for which `player[p]` was equal to `blud`.
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: `t` is a non-negative integer, `player` is a dictionary, `blud` is a list of two integers, and `out` is an empty list. All player identifiers in the original `out` have been printed with the message 'ELIMINATED'.
#Overall this is what the function does:The function `func_2` checks for players whose positions match the position of the Bludger (`blud`). If a match is found, it updates the player's position to `[-1, -1]` and prints the current time step (`t`), the player identifier, and the message 'ELIMINATED'. The function does not return any value.

