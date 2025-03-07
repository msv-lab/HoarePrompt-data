#State of the program right berfore the function call: obj is a list of two integers representing a position on the field, and d is a string representing a direction ('U', 'D', 'L', or 'R').
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
                #State: `obj` is a list of two integers where the second element is incremented by 1, given that `d` is 'R'.
            #State: Postcondition: `obj` is a list of two integers. If the direction `d` is 'L', the second element of `obj` is decremented by 1. If the direction `d` is 'R', the second element of `obj` is incremented by 1.
        #State: Postcondition: `obj` is a list of two integers. If the direction `d` is 'D', the first element of `obj` is incremented by 1. If the direction `d` is 'L', the second element of `obj` is decremented by 1. If the direction `d` is 'R', the second element of `obj` is incremented by 1.
    #State: Postcondition: `obj` is a list of two integers. If the direction `d` is 'U', the first element of `obj` is decremented by 1. If the direction `d` is 'D', the first element of `obj` is incremented by 1. If the direction `d` is 'L', the second element of `obj` is decremented by 1. If the direction `d` is 'R', the second element of `obj` is incremented by 1.
#Overall this is what the function does:The function `func_1` accepts a list `obj` containing two integers representing a position on a field and a direction `d` as a string ('U', 'D', 'L', or 'R'). It updates the position in `obj` based on the direction and returns the updated position. If `d` is 'U', the first element of `obj` is decremented by 1. If `d` is 'D', the first element is incremented by 1. If `d` is 'L', the second element is decremented by 1. If `d` is 'R', the second element is incremented by 1. After executing the function, `obj` will represent the new position on the field.

#State of the program right berfore the function call: t is an integer representing the current time (step) in the game, player is a dictionary mapping player identifiers (strings like 'R0', 'B0') to their current positions (a list of two integers [x, y]), and blud is a list of positions (a list of two integers [x, y]) representing the Bludgers on the field.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: Output State: `out` is a list containing player identifiers of those players whose positions matched any position in the `blud` list, and their positions in the `player` dictionary are updated to `[-1, -1]`. All other players and the `blud` list remain unchanged.
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: The list `out` contains player identifiers of those players whose positions matched any position in the `blud` list, and for each of these players, their positions in the `player` dictionary are updated to `[-1, -1]`. The loop prints each eliminated player's identifier along with the string 'ELIMINATED' in the sorted order of player identifiers. All other players and the `blud` list remain unchanged.
#Overall this is what the function does:The function processes the current state of players and Bludgers at time `t`. It identifies players whose positions match any Bludger position, marks them as eliminated by updating their positions in the `player` dictionary to `[-1, -1]`, and prints a message for each eliminated player in sorted order of their identifiers. The function does not return a specific value but modifies the `player` dictionary and prints elimination messages.

