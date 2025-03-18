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
                #State: `obj` is a list containing two integers representing the coordinates of an entity on the field. If `d` is 'R', the second integer in `obj` has been incremented by 1. The direction `d` is a string that can be 'D', 'L', or 'R', and it is not 'U' or 'D'. Additionally, `d` is not 'L'.
            #State: `obj` is a list containing two integers representing the coordinates of an entity on the field. If `d` is 'L', the second integer in `obj` is decreased by 1. If `d` is 'R', the second integer in `obj` is increased by 1. The direction `d` is a string that can be 'L' or 'R', and it is not 'U' or 'D'.
        #State: `obj` is a list containing two integers representing the coordinates of an entity on the field. If `d` is 'D', the first integer in `obj` is incremented by 1. If `d` is 'L', the second integer in `obj` is decreased by 1. If `d` is 'R', the second integer in `obj` is increased by 1. The direction `d` is a string that can be 'L', 'R', or 'D', and it is not 'U'.
    #State: `obj` is a list containing two integers representing the coordinates of an entity on the field. If `d` is 'U', the first element of `obj` is decreased by 1. If `d` is 'D', the first element of `obj` is increased by 1. If `d` is 'L', the second element of `obj` is decreased by 1. If `d` is 'R', the second element of `obj` is increased by 1. The direction `d` is a string that can be 'U', 'D', 'L', or 'R'.
#Overall this is what the function does:The function updates the coordinates of an entity on a field based on the specified direction of movement ('U', 'D', 'L', or 'R'). The function modifies the input list `obj` in place to reflect the new coordinates after the movement.

#State of the program right berfore the function call: t is a non-negative integer representing the current time step, player is a dictionary where keys are player identifiers (strings) and values are their current positions on the field (pairs of integers), and blud is a pair of integers representing the current position of the Bludger on the field.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: t is 0, player is {'Alice': [1, 2], 'Bob': [-1, -1], 'Charlie': [5, 6]}, blud is [3, 4], out is ['Bob']
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: t is 0, player is {'Alice': [1, 2], 'Bob': [-1, -1], 'Charlie': [5, 6]}, blud is [3, 4], out is ['Bob']
#Overall this is what the function does:The function `func_2` checks if any players are at the same position as the Bludger. If a player is found at the Bludger's position, their position is updated to `[-1, -1]`, indicating elimination, and their identifier is printed along with the current time step and the message 'ELIMINATED'. The function does not return any value.

