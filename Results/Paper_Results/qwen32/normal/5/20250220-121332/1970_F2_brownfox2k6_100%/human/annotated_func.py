#State of the program right berfore the function call: obj is a list of two integers representing the coordinates (row, column) of an entity on the field, and d is a string representing a direction ('U', 'D', 'L', 'R').
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
                #State: `obj` is a list of two integers representing the coordinates (row, column) of an entity on the field. If `d` is 'R', the column value of `obj` is incremented by 1. Since `d` is not 'U', 'D', or 'L', the only possible value for `d` is 'R', and thus the column value of `obj` is incremented by 1.
            #State: `obj` is a list of two integers representing the coordinates (row, column) of an entity on the field. If `d` is 'L', the column value of `obj` is decreased by 1. If `d` is 'R', the column value of `obj` is increased by 1. The direction `d` is not 'U' or 'D', and its value is either 'L' or 'R'.
        #State: `obj` is a list of two integers representing the coordinates (row, column) of an entity on the field. If `d` is 'D', the row value of `obj` is incremented by 1. If `d` is 'L', the column value of `obj` is decreased by 1. If `d` is 'R', the column value of `obj` is increased by 1. The direction `d` is not 'U'.
    #State: `obj` is a list of two integers representing the coordinates (row, column) of an entity on the field. If `d` is 'U', the row coordinate of `obj` is decremented by 1. If `d` is 'D', the row coordinate of `obj` is incremented by 1. If `d` is 'L', the column coordinate of `obj` is decremented by 1. If `d` is 'R', the column coordinate of `obj` is incremented by 1. The direction `d` is one of ('U', 'D', 'L', 'R').
#Overall this is what the function does:The function updates the coordinates of an entity on a field based on the specified direction ('U' for up, 'D' for down, 'L' for left, 'R' for right) by modifying the input list `obj` in place.

#State of the program right berfore the function call: t is a non-negative integer representing the current time step, player is a dictionary where keys are player identifiers and values are their positions on the field (as lists of two integers), and blud is a list of two integers representing the position of the Bludger on the field.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: t is 0, player is {'A': [-1, -1], 'B': [3, 4], 'C': [-1, -1]}, blud is [1, 2], out is ['A', 'C']
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: t is 0, player is {'A': [-1, -1], 'B': [3, 4], 'C': [-1, -1]}, blud is [1, 2], out is ['A', 'C', 'B']
#Overall this is what the function does:The function `func_2` updates the positions of players by setting their positions to `[-1, -1]` if they are at the same position as the Bludger. It also prints the identifiers of the eliminated players along with the current time step. The function does not return any value but modifies the `player` dictionary in place.

