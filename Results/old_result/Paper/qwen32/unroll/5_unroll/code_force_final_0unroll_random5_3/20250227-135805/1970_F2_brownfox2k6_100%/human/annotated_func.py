#State of the program right berfore the function call: obj is a list containing two integers representing the coordinates of an entity on the field, and d is a string that can be 'U', 'D', 'L', or 'R', representing the direction of movement.
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
                #State: `obj` is a list containing two integers representing the coordinates of an entity on the field. If `d` is 'R', the second integer in `obj` is incremented by 1. If `d` is not 'R', the list `obj` remains unchanged. The direction `d` can be 'L' or 'R'.
            #State: `obj` is a list containing two integers representing the coordinates of an entity on the field. If `d` is 'L', the second integer in `obj` is decreased by 1. If `d` is 'R', the second integer in `obj` is incremented by 1. If `d` is neither 'L' nor 'R', the list `obj` remains unchanged. The direction `d` can be 'L' or 'R'.
        #State: `obj` is a list containing two integers representing the coordinates of an entity on the field. If `d` is 'D', the first integer (y-coordinate) in `obj` is increased by 1. If `d` is 'L', the second integer (x-coordinate) in `obj` is decreased by 1. If `d` is 'R', the second integer (x-coordinate) in `obj` is incremented by 1. If `d` is neither 'D', 'L', nor 'R', the list `obj` remains unchanged. The direction `d` can be 'D', 'L', or 'R'.
    #State: `obj` is a list containing two integers representing the coordinates of an entity on the field. If `d` is 'U', the first integer (y-coordinate) in `obj` is decreased by 1. If `d` is 'D', the first integer (y-coordinate) in `obj` is increased by 1. If `d` is 'L', the second integer (x-coordinate) in `obj` is decreased by 1. If `d` is 'R', the second integer (x-coordinate) in `obj` is incremented by 1. If `d` is neither 'U', 'D', 'L', nor 'R', the list `obj` remains unchanged.
#Overall this is what the function does:The function updates the coordinates of an entity on a field based on a specified direction ('U' for up, 'D' for down, 'L' for left, 'R' for right). The function modifies the input list `obj` directly to reflect the new coordinates after the movement.

#State of the program right berfore the function call: t is a non-negative integer representing the current time step, player is a dictionary where keys are player identifiers (strings) and values are their positions on the field (pairs of integers), and blud is a pair of integers representing the position of the Bludger on the field.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: t = initial t value, player = updated player dictionary with positions of players matching blud set to [-1, -1], blud = initial blud value, out = list of player identifiers whose positions matched blud
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: t = initial t value, player = updated player dictionary with positions of players matching blud set to [-1, -1], blud = initial blud value, out = list of player identifiers whose positions matched blud
#Overall this is what the function does:The function `func_2` processes the positions of players and the Bludger on a field. It identifies players whose positions match the Bludger's position, sets their positions to `[-1, -1]`, and prints their identifiers along with the current time step and the message 'ELIMINATED'. The function modifies the `player` dictionary in place and does not return any value.

