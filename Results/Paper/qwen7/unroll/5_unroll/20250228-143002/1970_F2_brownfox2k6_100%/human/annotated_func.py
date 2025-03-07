#State of the program right berfore the function call: obj is a list of two integers representing a position on the field (row, column), and d is a string representing the direction of movement ('U', 'D', 'L', or 'R').
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
                #State: `obj` is a list of two integers where the second element is increased by 1, because the direction `d` is 'R'.
            #State: Postcondition: `obj` is a list of two integers representing a position on the field. If the direction `d` is 'L', the column (second element) of `obj` is decremented by 1. If the direction `d` is 'R', the column (second element) of `obj` is incremented by 1.
        #State: Postcondition: `obj` is a list of two integers representing a position on the field. If the direction `d` is 'D', the row (first element) of `obj` is incremented by 1. If the direction `d` is 'L', the column (second element) of `obj` is decremented by 1. If the direction `d` is 'R', the column (second element) of `obj` is incremented by 1.
    #State: Postcondition: `obj` is a list of two integers representing a position on the field. If the direction `d` is 'U', the row (first element) of `obj` is decremented by 1. If the direction `d` is 'D', the row (first element) of `obj` is incremented by 1. If the direction `d` is 'L', the column (second element) of `obj` is decremented by 1. If the direction `d` is 'R', the column (second element) of `obj` is incremented by 1.
#Overall this is what the function does:The function `func_1` accepts a position on a field represented by a list of two integers (`obj`) and a direction of movement (`d`). Based on the direction, it updates the position by moving up ('U'), down ('D'), left ('L'), or right ('R'). After the movement, it returns the updated position as a list of two integers.

#State of the program right berfore the function call: t is an integer representing the current time step in the game. player is a dictionary where keys are player identifiers (e.g., 'R0', 'B0') and values are their current positions represented as [row, column] lists. blud is a list of positions where the Bludger is currently located.
def func_2(t):
    out = []
    for p in player:
        if player[p] == blud:
            out.append(p)
            player[p] = [-1, -1]
        
    #State: Output State: `out` is a list containing player identifiers of those players whose positions matched with the Bludger's position. `t` is an integer representing the current time step in the game. `player` is a dictionary where keys are player identifiers and values are their current positions, with any player whose position matched the Bludger's position updated to `[-1, -1]`. `blud` is a list of positions where the Bludger is currently located.
    for p in sorted(out):
        print(t, p, 'ELIMINATED')
        
    #State: Output State: The console prints each player identifier `p` from the sorted list `out`, along with the current time step `t`, followed by the string 'ELIMINATED'. This means that for each player whose position matched the Bludger's position, the game prints a statement indicating that the player has been eliminated at the current time step.
#Overall this is what the function does:The function processes the current positions of players and the Bludger at a given time step in the game. It identifies any players whose positions match the Bludger's position and marks them as eliminated by updating their positions to `[-1, -1]`. The function then prints a message for each eliminated player indicating they have been eliminated at the current time step.

