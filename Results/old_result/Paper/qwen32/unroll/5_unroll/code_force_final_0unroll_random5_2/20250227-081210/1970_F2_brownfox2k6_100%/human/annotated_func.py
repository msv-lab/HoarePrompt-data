#State of the program right berfore the function call: obj is a list of two integers representing the coordinates of an entity on the field, and d is a character that can be 'U', 'D', 'L', or 'R', representing the direction of movement.
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
                #State: `obj` is a list of two integers representing the coordinates of an entity on the field. If `d` is 'R', the second integer (y-coordinate) of `obj` has been incremented by 1. `d` is a character that can be 'R' or 'D', and `d` is not equal to 'U'. If `d` is 'D', the coordinates of `obj` remain unchanged.
            #State: `obj` is a list of two integers representing the coordinates of an entity on the field. If `d` is 'L', the second integer (y-coordinate) of `obj` is decreased by 1. If `d` is 'R', the second integer (y-coordinate) of `obj` is incremented by 1. If `d` is 'D', the coordinates of `obj` remain unchanged. `d` is a character that can be 'L', 'R', or 'D', and `d` is not equal to 'U'.
        #State: `obj` is a list of two integers representing the coordinates of an entity on the field. If `d` is 'D', the first integer (x-coordinate) of `obj` is incremented by 1. If `d` is 'L', the second integer (y-coordinate) of `obj` is decreased by 1. If `d` is 'R', the second integer (y-coordinate) of `obj` is incremented by 1. `d` is a character that can be 'L', 'R', or 'D', and `d` is not equal to 'U'.
    #State: `obj` is a list of two integers representing the coordinates of an entity on the field. If `d` is 'U', the first integer (x-coordinate) of `obj` is decreased by 1. If `d` is 'D', the first integer (x-coordinate) of `obj` is incremented by 1. If `d` is 'L', the second integer (y-coordinate) of `obj` is decreased by 1. If `d` is 'R', the second integer (y-coordinate) of `obj` is incremented by 1. `d` is a character that can be 'U', 'D', 'L', or 'R'.
#Overall this is what the function does:The function `func_1` modifies the input list `obj`, which represents the coordinates of an entity on a field, by updating these coordinates based on the direction specified by the character `d`. The direction `d` can be 'U' (up), 'D' (down), 'L' (left), or 'R' (right). After the function call, `obj` contains the new coordinates of the entity after moving in the specified direction.

#State of the program right berfore the function call: t is a non-negative integer representing the current time step, player is a dictionary where keys are player identifiers (strings like 'R0', 'B1', etc.) and values are lists of two integers representing their positions on the field, and blud is a list of two integers representing the position of the Bludger on the field.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: t = 0, player = {'R0': [1, 2], 'B1': [-1, -1], 'G2': [5, 6]}, blud = [3, 4], out = ['B1']
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: t = 0, player = {'R0': [1, 2], 'B1': [-1, -1], 'G2': [5, 6]}, blud = [3, 4], out = ['B1']
#Overall this is what the function does:The function `func_2` processes a list of players and the position of a Bludger. It checks if any player is at the same position as the Bludger and, if so, marks that player as eliminated by setting their position to `[-1, -1]`. It then prints out the time step and the identifier of each eliminated player. The function does not return any value.

